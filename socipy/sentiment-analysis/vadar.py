#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from typing import Tuple, List, Dict

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia

nltk.download('punkt')
nltk.download('vader_lexicon')


class Vadar(sia):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
    def _preprocess(self, corpus: str) -> List:
        return nltk.tokenize.sent_tokenize(corpus)

    def batch_predict(self, corpus: str) -> Tuple[List, List[Dict]]:
        scores = []
        sents = self._preprocess(corpus)
        for sent in sents:
            if sent:
                scores.append(self.polarity_scores(sent))
        
        return sents, scores

def main():
    print("Demo start")
    corpus = input("Key in a list of sentences or one sentence to test sentiments:\n")
    analyzer = Vadar()
    sents, scores = analyzer.batch_predict(corpus)
    for (x,y) in zip(sents, scores):
        print('sentence:',x,'; score:',y)
    print('Demo finish')

if __name__ == "__main__":
    main()