#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import tika
from tika import parser
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',"--path2folder",default='',type=str)
    parser.add_argument('-d',"--deleteall",default=False,type=bool)

    args = parser.parse_args()
    return args

def pdf2txt(path2folder='', deleteall=False):
    """Convert pdf-format files into plain text files.

    Args:
        path2folder (str): path to folder of files that need convertion. Default to current directory.
        deleteall (bool): if set to True, it deletes all original pdf files (useful 
        when they occupy large memory space)
    """
    filepath = path2folder if path2folder else os.curdir

    files = os.listdir(filepath)

    tika.initVM()

    for file in files:
        if file.endswith('.pdf'):
            parsed = parser.from_file(os.path.join(filepath,file))
            text = parsed["content"]

            save_f = open(f'{file[:-4]}.txt','w',errors="ignore")
            save_f.write(text)
            print(f'{file[:-4]}.txt write')
            
            save_f.close()

            if deleteall:
                os.remove(os.path.join(filepath,file))
                print(f'{file} removed')

def main():
    args = parse_args()
    pdf2txt(args.path2folder, args.deleteall)


if __name__ == '__main__':
    main()