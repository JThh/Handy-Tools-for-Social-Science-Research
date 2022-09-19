# Socipy: Handy Tools for Social Science Research

## Motivation

This repository contains a list of frequently used research utilities (actively growing) when I did many interdisciplinary research assistant jobs (especially related to public policy and economics research). The tools span across the areas of natural language processing (e.g. sentiment analysis, text classification), social network analysis, and file stream processing. 

Many tools are the outcome of collaboration, and I have given credit in the relevant section. Notably, thanks to many professors (such as [Prof. Min-Yen Kan](https://www.comp.nus.edu.sg/~kanmy/), [Prof. Bimlesh Wadhwa](https://www.comp.nus.edu.sg/cs/people/bimlesh/) and [Prof. Yuhao Ba](https://lkyspp.nus.edu.sg/our-people/faculty/ba-yuhao)) and researchers (such as [Dr. Lucas Shen](https://www.lucasshen.com/)) that have advised or hired me and let me help them accomplish these tools. I hope open sourcing and automating their use can help more social science researchers and workers to less rely on computer science professionals.

I welcome contributors (especially social science researchers) to give advice or contribute codes.

I am working on modularizing the codes and designing the interfaces; do star the project and check out the progress! (Hope I can at least half-finish it before recess ends) 

## Get Started
It has (yet) been packaged as a `pip` library named 'socipy'.

 <!-- To install, run the following command: -->
<!-- ```
python3 -m pip install socipy
``` -->

For now, to install it manually, run:
```
git clone https://github.com/JThh/Handy-Tools-for-Social-Science-Research.git socipy
cd socipy
python3 setup.py install
```

## Categories

For easier navigation, I have sorted them in a table and made separate instruction file in each sub-folder. The table is continuously growing and the tools are being actively maintainly. Please raise an issue should there be any problem in using the tools. 

| Tool      | Keywords | progress |
| ----------- | ----------- | ----------- |
| [File Conversion](./socipy/file-conversion/)   | RTF-to-TXT, PDF-to-TXT, Web Scraping         | **Finished!** |
| [Sentiment Analysis](./socipy/sentiment-analysis/)      | Models, Visualizations, and Emotions       | _Unfinished_ |
| [Social Network Analysis](./socipy/social-network-analysis/)   | Data processing, Visualization, Network Properties         | _Unfinished_ |
| [Text Classification](./socipy/text-classification/)   | (Pretrained) Models, (Un-)Supervised Classification         | _Unfinished_ |
