import os
import re
import argparse
from typing import Tuple, List
from collections import OrderedDict

import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


lemmatizer = WordNetLemmatizer()
pretrained_embeddings: dict = None


def parse_args():
    parser = argparse.ArgumentParser('parser for input and output paths')
    parser.add_argument('-i','--input_folder',type=str,help='path to input folders (containing a list of folders)')
    parser.add_argument('-k','--keyword_file',type=str)
    parser.add_argument('-p','--pretrained_embeddings',type=str,help='path to pretrained embeddings')
    parser.add_argument('-n','--ngrams',type=str,default='2-4',help='ngrams used for tf-idf weighting with the format of "start-end"')
    parser.add_argument('-o','--output_file',type=str,default='./output.csv')
    args = parser.parse_args()
    return args

def combine_files(dir: str, files: List[str]):
    result = ''
    for file_path in files:
        assert os.path.exists(os.path.join(dir, file_path))
        with open(os.path.join(dir, file_path), 'r') as f:
            result += f.read()
    return result

def preprocess(text: str):
    global lemmatizer
    keywords = re.sub('[\W_]+', '', text)
    keyword_list = word_tokenize(keywords)
    lemma_keyword_list = [lemmatizer.lemmatize(kw) for kw in keyword_list]
    return lemma_keyword_list

def load_pretrained_embeddings(path):
    global pretrained_embeddings
    assert os.path.exists(path)
    pretrained_embeddings = {}
    f = open(path, "r")
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        pretrained_embeddings[word] = coefs
    f.close()
    print('Pretrained embeddings successfully loaded into environment.')

def get_keyword_embedding(keywords: str):
    global pretrained_embeddings
    keyword_list = preprocess(keywords)
    embeddings = {}

    for kw in keyword_list:
        if kw in pretrained_embeddings:
            embeddings[kw] = np.asanyarray(pretrained_embeddings[kw])
    
    if embeddings:
        return embeddings, len(embeddings[kw])
    else:
        return None, None

def get_tfidf_weights(corpus: List[str], ngrams: Tuple = (2,3,4)):
    vectorizer = TfidfVectorizer(ngrams_range=ngrams)
    X = vectorizer.fit_transform(corpus)
    return X, vectorizer.get_feature_names_out()

def get_corpus_embedding(data_dict: OrderedDict):
    if not data_dict: 
        return
    result_dict = {}
    weights, features = get_tfidf_weights(list(data_dict.values()))

    for (name, corpus) in data_dict.items():
        embeds, dim = get_keyword_embedding(corpus)
        index = list(data_dict.keys()).index(name)
        agg_embed = np.zeros(dim)
        for i in range(len(features)):
            featurei = features[i]
            if featurei in embeds:
                weight = weights[index][i]
                embed = embeds[featurei]
                agg_embed += weight * np.asarray(embed)
        result_dict[name] = agg_embed

    return result_dict

def get_similarity(corpus_embed: dict, keyword_embed: dict):
    def cosine_similarity(a, b):
        assert len(a) == len(b)
        return np.dot(a, b) / (np.norm(a) * np.norm(b))

    result_dict = {}

    for (corpus, cp_embed) in corpus_embed.items():
        cp_scores = []
        for (keyword, kw_embed) in keyword_embed.items():
            score = cosine_similarity(cp_embed, kw_embed)
            cp_scores.append(score)
        result_dict[corpus] = cp_scores
        
    return pd.DataFrame.from_dict(result_dict, orient='index')

def main():
    args = parse_args()
    print('---start processing---')
    load_pretrained_embeddings(args.pretrained_embeddings)

    with open(args.keyword_file, 'r') as f:
        keyword_string = f.read()
        keyword_embed = get_keyword_embedding(keyword_string)

    args.input_folder = args.input_folder.strip('/')
    dirs = os.listdir(args.input_folder)
    data_dict = OrderedDict()
    for dir in dirs:
        name = dir.split('/')[-1]
        if os.path.isdir(dir):
            data_dict[name] = combine_files(args.input_folder + '/' + name, os.listdir(dir))
        else:
            with open(dir, 'r') as f:
                data_dict[name] = f.read()

    corpus_embed = get_corpus_embedding(data_dict)
    scores = get_similarity(corpus_embed, keyword_embed)
    scores.to_csv(args.output_file, index=False)

if __name__ == '__main__':
    main()