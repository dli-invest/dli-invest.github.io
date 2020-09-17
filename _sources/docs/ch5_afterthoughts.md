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
6. Does the stock have good managemen

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