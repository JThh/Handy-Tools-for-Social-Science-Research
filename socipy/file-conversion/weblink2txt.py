#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
import os
import urllib.request
import argparse
import time

# Real URL scraped for my RA job
EXAMPLE_URL = "https://www.congress.gov/congressional-report/115th-congress/senate-report/125/1,%22115th"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',"--savepath",default='',type=str)
    parser.add_argument('-u',"--url",default=EXAMPLE_URL,type=str)
    args = parser.parse_args()
    return args

def weblink2txt(url, savepath):
    """Scrape web page contained text files and store them locally.

    Args:
        url (str): path to web page which contains a preview section of text contents.
        savepath (str): directory/file path to save scraped web texts.
    """
    if not savepath:
        savepath = os.curdir()

    file = open(os.path.join(savepath,f"webscrapedtext{time.asctime()}.txt"), 'w')

    # get html from web url
    try:
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data = response.read() 
        html = data.decode("utf8")
        response.close()

        # process html and get text preview
        soup = BeautifulSoup(html, 'html.parser')
        previews = soup.find_all('pre')
        for url in previews:
            text = url.get_text()
        file.write(text)
    except Exception as e: # incase of any error (web request or file saving)
        print(e)

    file.close()


def main():
    args = parse_args()
    weblink2txt(args.url, args.savepath)


if __name__ == '__main__':
    main()