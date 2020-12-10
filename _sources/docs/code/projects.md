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

# Stock Investing Projects

Contains project overview and what I seek to accomplish in each project.

### Youtube NLP

* Annotate youtube videos
* v2 can annotate videos without youtube transcriptions

### Investing Book

* Executable book containing all the content for my investing journey from software engineer
to successful investor.
* Contains a list of projects I have built related for investing.

### Stock Dashboard

* Includings various dash and streamlit apps for ta and analysis of stocks. My most common use case is to 
just look at all the stock prices of things I am interested in.
* Dashboard with links to other projects

### Earnings Report Calendar

* Creates events in my calendar when the stocks in my stock list are being generated
* Cron job to update list of stocks of interest
* Copy existing google calendar interaction code from repo
* Use best practise to initialize python repo
* Have discord webhook to notify success or failure
* update csv containing captured earnings per week (useful for future trading) - index by id
* use browserstack instead of selenium for visiblity and easier traceback.
* Make open source under dli-invest.


### News Alerts

* Output notifications from yahoo news, this only gets recent news, sometimes there is clutter from ads and/or random new items, but good enough for my purposes

### 2021

#### Bid analysis

Get bid data per market open - move into fast api???

Need to get bids for stocks from tmx web money and the cse before market open (might need selenium, probably not).
