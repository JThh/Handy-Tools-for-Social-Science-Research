# File Conversion

## Quick Start

For a quick start, run the bash file:

```
export DIR='./data/' # directory containing files to convert; change accordingly
./batch.sh
```

## Explanation

Each utility has very similar usage; make sure to check out `parse_args()` function from each file.

- `pdf2txt.py` requires an input path to a folder and it converts all pdf files contained in the folder into text files; optionally it can help delete all pdf files after convertion;
 
- `rtf2txt.py` works in exactly the same way, except that it deals with rich text files;

- `weblink2txt.py` requires an input URL and an address to save scraped texts from the web link. It is further required that the web page should have a `preview` section header and is legal to scrape.

## Credit

Credit specifically given to Prof. Yuhao Ba and myself.