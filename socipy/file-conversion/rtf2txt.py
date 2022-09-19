#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from striprtf.striprtf import rtf_to_text
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',"--path2folder",default='',type=str)
    parser.add_argument('-d',"--deleteall",default=False,type=bool)

    args = parser.parse_args()
    return args

def rtf2txt(path2folder='', deleteall=False):
    """Convert rtf-format (rich text files) into plain text files.

    Args:
        path2folder (str): path to folder of files that need convertion. Default to current directory.
        deleteall (bool): if set to True, it deletes all original rtf files (useful 
        when they occupy large memory space)
    """
    filepath = path2folder if path2folder else os.curdir

    files = os.listdir(filepath)

    for file in files:
        if file.endswith('.rtf'):
            f = open(os.path.join(filepath,file),'r',encoding='gbk',errors="ignore")
            rtf = f.read()
            text = rtf_to_text(rtf, errors="ignore")
            print(f'{file} read')
            
            save_f = open(os.path.join(filepath,f'{file[:-4]}.txt'),'w',errors="ignore")
            save_f.write(text)
            print(f'{file[:-4]}.txt write')
            
            f.close()
            save_f.close()

            if deleteall:
                os.remove(os.path.join(filepath,file))
                print(f'{file} removed')


def main():
    args = parse_args()
    rtf2txt(args.path2folder, args.deleteall)


if __name__ == '__main__':
    main()