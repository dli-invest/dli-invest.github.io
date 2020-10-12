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

(Afterthoughts)=
# Afterthoughts

One of my early purchase as an investor has been victory square.

### Decision Making Framework
1. Never buy a stock expecting to make money
2. Does the stock have momentum
3. Is this a good time to buy this stock and why (good news not realised, or no interest)
4. Do I expect the stock to go up
5. Is this stock industry going to be useful and do well
6. Does the stock have good management.


## Stock Purchases Thoughts

**10/11/2020**

Doubling down on peak as some guy in ceo.ca/pkk posted an article about china growing. They have control of the virus, it makes sense to invest in a country that is growing that is not in the state, espeically if they believe they are severely undervalued with high margins and the opportunity to give a dividend.

In addition, sheldon has a position in pkk.

Cielo seems to be doing well, if production numbers are 1000 L/h (pretty high), I would expect 100x return sometime in the future. After all, they have done the work to start growing like crazy as plastic production is projected to increase and there is no solution as good as cielo at the moment.

**09/11/2020**

**09/13/2020**
KUU MIGHT BEINSOVLENT
Wait on BYL for 5G

Think about VIS.V if it makes 334,250 as projected in Q4

The stocks I looked at recently that were interesting as of 09/15/2020

| Ticker   | Long Name                       |
| :---     | ---:                            |
| PAI      | Predictiv AI Inc.               |
| RW       | RenoWorks Software Inc          |
| DFT      | Dimension Five Technologies Inc |
| KUU      | Kuuhubb Inc                     |
| BYL      | Baylin Technology Inc           |
| CMC      | Cielo Waste Solutions Inc       |


**09/08/2020**
```{code-cell} ipython3
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf

vst = yf.Ticker("VST.CN")
data = vst.history(interval="1d", start_date="08-08-2020", end_date="09-08-2020")
mpf.plot(
    data,
    type="candle",
    mav=4,
    title="Victory Square Purchases Dates",
    vlines=dict(
        vlines=["08-26-2020", "09-03-2020", "09-08-2020"], linewidths=(0.5, 0.5, 0.5)
    ),
)
```

The first few purchases on August 26 and September 03 were profitable, after the failed Sept 08 purchases and surprise drop I emailed the investor relations guy asking about india approval.

My brief calculations of the covid-19 test selling well make me think if they sell well (80 \%), the stock will continue the rise.

The combination of covid-19 increasing, the need to know if you were previously infected for health care workers perhaps even vaccines, make me think that the stock will go up in the short term in the next few months.




### Cloud Architecture V0

As for sept 28 2020

```{figure} /_static/diagrams/v0stockarch.png
```

my basic cloud archtecture was based on gcp. Primarily using google cloud build for automated deployed and the various serverless compute options. Aimed to stay within free tier but sometimes I paid cash for this (TODO make a blog post about my stocks hosting stuff).
