---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(utility_code)=
# Web Scrapping and Data Extraction

Oftentimes, there is data available on the internet and/or in files in which you want specific parts. When I was reading finance books and technical books I found it incredibly useful to extract tables from pdfs. Below is the code I use to extract data, note that camelot requires (tk and ghostscript).

% Add reference for camelot

As someone who has gone through university using latex, it was only natural for me to want to convert content locked in pdf into formats useful to me.

```python
"""
extractTables.py
    --- Takes tables from pdf documents and then outputs latex tables
"""
__author__ = "David Li"
import os
import argparse 
import pandas as pd
import camelot
import glob
import io
from os import makedirs, listdir, removedirs, chdir
from os.path import isfile, exists, splitext

pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 3000)
# See https://gist.github.com/marianoguerra/1137302
import sys
import csv
import pytablewriter

def to_rst(csv_path, rst_path='default.tex'):
    '''
    to convert a csv table to rst
    '''
    try:
        print(csv_path)
        # process(in_=path, out=None, title=title)
        writer = pytablewriter.RstGridTableWriter()
        writer.table_name = "example_table"
        rst_df = pd.read_csv(str(csv_path))
        print(rst_df)
        writer.from_dataframe(rst_df)
        with open(rst_path, 'w') as rst_f:
            rst_f.write(writer.dumps())
    except:
        print('Unable to write to file')

def to_tex(csv_path, tex_path='default.tex'):
    '''to convert a csv table to tex using pandas'''
    try:
        tex_df = pd.read_csv(str(csv_path))
        tex_df.to_latex(tex_path,longtable=True)
    except:
        print('Unable to write to file')

def mkdir_new(folder_name='2019-01-03'):
    """Makes a new directory if it doesn't already exist"""
    if not exists(folder_name):
        makedirs(folder_name)

def main(args):
    # In general I like hardcoding the file name
    pdf_file = f'Stefan Jansen - Machine Learning for Algorithmic Trading_ Predictive models to extract signals from market and alternative data for systematic trading strategies with Python, 2nd Edition (2020, Packt Publishing) - li.pdf'
    path_to_file = os.path.join('C:/', 'Users', 'stude', 'Desktop', pdf_file)
    tables = camelot.read_pdf(path_to_file, pages='118,119')

    dir_name = 'temp'
    mkdir_new(dir_name)
    # tables = camelot.read_pdf('C++.pdf', pages='2-end')
    tables.export('{}/{}'.format(dir_name, 'temp.csv'), f='csv', compress=False)
    # iterate across all produced csvs and produce rst or tex
    for file_name in list(glob.glob("temp/*.csv")):
        if args.rst:
            # consider saving rst in different folder 
            rst_name = '{}.{}'.format(splitext(file_name)[0], 'rst')
            to_rst(file_name, rst_name)
        if args.tex:
            tex_name = '{}.{}'.format(splitext(file_name)[0], 'tex')
            to_tex(file_name, tex_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", 
                        "--pdf", 
                        help="Pdf Document with pages", 
                        default="C++.pdf") 
    parser.add_argument("-pa", 
                        "--pages", 
                        help="Pdf document Pages",
                        default="2-end") 
    parser.add_argument("-rst", 
                      "--rst_tables", 
                      help="Take outputted csvs and convert to restructured text using pandoc",
                      default="Bad Password")
    parser.add_argument('--rst', dest='rst', action='store_true')
    parser.add_argument('--no-rst', dest='rst', action='store_false')
    parser.add_argument('--feature', dest='feature', action='store_true')
    parser.add_argument('--no-feature', dest='feature', action='store_false')
    parser.add_argument("-tex", 
                      "--latex", 
                      help="Take outputted csvs and convert to latex using pandas",
                      action="store_true"
                      ) 
    parser.set_defaults(rst=True, tex=True)

    args = parser.parse_args()

    main(args)
```

The following utility scripts uses camelot to extract tables from pdf and then save them in `rst` format, it has difficult merging tables split around 2 pages which is why I save the individual `csvs` files.

Some sample output can be seen at {ref}`some_value_factors`