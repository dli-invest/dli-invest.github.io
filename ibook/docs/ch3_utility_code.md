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

% Consider adding this code to appendix

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

Some sample output can be seen at {ref}`some_value_factors`, {numref}`some_value_factors`


Another script that I have used is for converting glossary for the latex format to something that jupyterbook can understand, the script is very rough and does not work with references to terms within terms. `\glsapi{}` will be inputted as raw latex, I am expecting the excecutable book project to eventually produce a better solution, but in the interim this script looks for my purposes.

```python
"""
Converts a tex glossary into a format jupyterbook can understand

Extended from https://tex.stackexchange.com/questions/529971/how-do-i-sort-all-of-the-glossary-entries-in-a-tex-file
"""

import argparse
import os
import re
import webbrowser
from collections import OrderedDict

commands = (r"\\newglossaryentry", r"\\newabbreviation", r"\\newacronym")
startcmd_regex = re.compile(
    r"(?:" + r"|".join(commands) + r")\s*\r?\n?\s*\{(.+?)\}\s*\r?\n?\s*\{"
)
brace_regex = re.compile(r"(?<!\\)(?:\\\\)*(\{|\})")


class UnreachableError(Exception):
    def __init__(self, *args, **kwargs):
        webbrowser.open("https://xkcd.com/2200/")
        super().__init__(
            "The code is in what I thought was an unreachable state.", *args, **kwargs
        )


class ParseError(Exception):
    pass


def scan_file(fname):
    """
    Scan a file and separate it into entries and outer code.

    Parameters
    ----------
    fname : str
        The file name.

    Raises
    ------
    ParseError
        If the end of an entry cannot be found.
    UnreachableError
        If a state is reached that should be unreachable.

    Returns
    -------
    entries : dict
        The entries.
        entries[None] always containes the collected outer code.

    """
    with open(fname, "r", errors="ignore") as rf:
        text = rf.read()
    open_braces = 0
    entries = {None: ""}
    label = None
    while text:
        if label is None:
            # Look for next entry.
            match = startcmd_regex.search(text)
            if match is None:
                piece = text.strip()
                if piece:
                    entries[label] += piece + "\n"
                text = ""
            else:
                piece = text[0 : match.start()].strip()
                if piece:
                    entries[label] += piece + "\n"
                label = match.group(1)
                if label in entries:
                    entries[label] += "\n"
                else:
                    entries[label] = ""
                entries[label] += match.group(0).lstrip()
                open_braces = 1
                text = text[match.end() :]
        else:
            # Look for next brace.
            match = brace_regex.search(text)
            if match is None:
                raise ParseError(
                    "I could not find all closing braces in "
                    + "'{}' ({} open braces)!".format(label, open_braces)
                )
            else:
                entries[label] += text[: match.end()]
                text = text[match.end() :]
                brace = match.group(1)
                if brace == "{":
                    open_braces += 1
                elif brace == "}":
                    open_braces -= 1
                else:
                    raise UnreachableError
                if open_braces == 0:
                    # This entry is done.
                    label = None
                elif open_braces < 0:
                    raise UnreachableError
    return entries


def sort_entries(source, *, label_sort=False):
    """
    Sort all the entries in the source file and returns and dict

    Parameters
    ----------
    source : str
        The name of the source file.
    label_sort : bool, optional
        If True, the entries are sorted by their label, otherwise they are
        sorted by their definition (including the definition command).
        The default is False.

    Raises
    ------
    ValueError
        If the source file cannot be found.

    Returns
    -------
    None.

    """
    present_files = os.listdir()
    if source not in present_files:
        raise ValueError("I cannot find the file '{}'!".format(source))
    entries = scan_file(source)
    return entries


def dict_with_descr(entries: dict):
    new_entries = {}
    for key in entries:
        if key == None:
            continue
        else:
            glossary_entry = entries[key]
            split_content = glossary_entry.split("description", 1)[1]
            # replace { } and \t \n
            cleaned_content = re.sub("{|}|\\t|\\n|=", "", split_content)
            # to extract words from string
            description = cleaned_content
            new_entries[key] = description

    return new_entries


def make_glossary(descriptions: dict):
    gloss_open = r"```{glossary}"
    gloss_end = r"```"
    body = ""
    # sort keys first
    for desc_key in sorted(descriptions.keys()):
        body = body + f"{desc_key}\n\t{descriptions[desc_key]}"
        body = body + "\n\n"
    return f"{gloss_open}\n{body}\n{gloss_end}"


def main():
    parser = argparse.ArgumentParser(description="Sort the glossary entries in a file.")
    parser.add_argument("-l", "--label-sort", action="store_true")
    parser.add_argument("source", help="The source file.")
    args = parser.parse_args()
    entries = sort_entries(args.source, label_sort=args.label_sort)
    descriptions = dict_with_descr(entries)
    glossary_str = make_glossary(descriptions)
    with open('glossary_data.md', 'w') as _f:
        _f.write(glossary_str)


if __name__ == "__main__":
    main()
```

For an example glossary file with the contents 


```tex
\newglossaryentry{DebtToEquity}
{
	name={Debt To Equity},
	description={
		The debt-to-equity (D/E) ratio indicates how much debt a company is using to finance its assets relative to the value of shareholders' equity.
	}
}

\newglossaryentry{DeadCatBounce}
{
	name={Dead Cat Bounce},
	description={
		Dead cat bounce is a small, brief recovery in the price of a declining stock.
	}
}
```

We would expect this script to output, this is really only useful if you are seeking to produce/convert jupyterbook content.

```tex
{glossary}
DeadCatBounce
        Dead cat bounce is a small, brief recovery in the price of a declining stock.

DebtToEquity
        The debt-to-equity (D/E) ratio indicates how much debt a company is using to finance its assets relative to the value of shareholders' equity.
```

