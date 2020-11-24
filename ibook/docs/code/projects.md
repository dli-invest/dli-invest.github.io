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

## Earnings Report Calendar

* Creates events in my calendar when the stocks in my stock list are being generated
* Cron job to update list of stocks of interest
* Copy existing google calendar interaction code from repo
* Use best practise to initialize python repo
* Add discord webhook to notify success or failure
* update csv containing captured earnings per week (useful for future trading) - index by id
* use browserstack instead of selenium for visiblity and easier traceback.
* Make open source under dli-invest.


## Sedar documents

The sedar documents site is horribly outdated, I can automatically grab and download documents


Steps:
Seleinum based.

1. Go to inputted sedar url
2. Click on given link 
3. capcha reading using ocr downloading 5 images
4. entering data into input field
5. visiting all the other links now that authentication has occured.