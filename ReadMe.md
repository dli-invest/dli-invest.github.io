# Investing Book

This is my a interactive recording of my quest to become a successful investor.

Contains various code snippets in python and ipython notebooks with useful code snippets to analyze a variety of stocks and stock related data.

My quest to gain an edge on stocks includes

* Scanning for news from yahoo
* Subscribing to ceo.ca to get news alerts
* Python scripts to visualize my yolo purchase decisions
* Sentiment Analysis on published documents and text
* Analyze the transcripts of youtube videos for nlp
* Algorithmic trading - just for back testing
* Price Prediction
* Risk Analyze - I honestly just held enough cash to deploy in any situation.
* Estimation of Returns

But to be perfectly honest, I have done fairly well buying canadian small cap companies that were interesting or undervalued in 2021, not 2022.


### Building this book

To build this project

```
jb build ibook/
```

To convert an ipynb book to a markdown file
```
jupytext CorrelationExamples.ipynb --to rmarkdown
```

Since this book contains useful contain, I will try to make money on ads, please click on them <3


To serve content directly you can use

```python
python -m http.server 8080 --bind 127.0.0.1 --directory ibook/_build
```


This repo is meant to contain some of my investing notes