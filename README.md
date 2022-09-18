# Handy Tools for Social Science Research

## Motivation

This repository contains a list of frequently used research utilities when I did many social science related RA jobs (especially related to public policy and economics research). The tools span across the areas of natural language processing (e.g. sentiment analysis, text classification), social network analysis, or file stream processing. 

Many tools are the outcome of collaboration, and I have given credit in the relevant section. Notably, thanks to many professors and researchers that have hired me and let me help them accomplish these tools. I hope open sourcing and automating their use can help more social science researchers and workers to less rely on computer science professionals.

I welcome contributors (especially social science researchers) to give advice or contribute codes.

## Get Started
It has been packaged as a `pip` library named 'socipy'. To install, run the following command:
```
python3 -m pip install socipy
```

To install it manually, run:
```
git clone https://github.com/JThh/Handy-Tools-for-Social-Science-Research.git socipy
cd socipy
python3 setup.py install
```

## Categories

For easier navigation, I have sorted them in a table and made separate instruction file in each sub-folder. The table is continuously growing and the tools are being actively maintainly. Please raise an issue should there be any problem in using the tools. 

| Tool      | Keywords |
| ----------- | ----------- |
| [Sentiment Analysis](./socipy/sentiment-analysis/README.md)      | Models, Visualizations, and Emotions       |
| [Social Network Analysis](./socipy/social-network-analysis/README.md)   | Data processing, Visualization, Network Properties         |
| [Text Classification](./socipy/text-classification/README.md)   | (Pretrained) Models, (Un-)Supervised Classification         |
| [File Conversion](./socipy/file-conversion/README.md)   | RTF-to-TXT, PDF-to-TXT, Web Scraping         |
