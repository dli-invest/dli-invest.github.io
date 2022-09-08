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

# 2022 Stonk thoughts


## Itafos
analysis can be performed better here.

Itafos stock valued about slightly above 3 PE. Given general food shortages and high fertilizer prices, would expect the value here to stay, even alternative producers like earth renew are going to need phosphate rock.

With market downturn, its possible this stock will go to 2 or 1 PE, net debt is acceptable.

They expect a slowing in H2 2022 as no one has money anymore.

Decent amount of shareholder equitity

214414000 USD, market cap

```{code-cell} ipython3

jun22_equitity = 214414	* 1000
# market cap in usd
market_cap =363.735 * 1000 * 1000

# ratio is
ratio = jun22_equitity / market_cap
print(ratio)
```

So if the business is liquidized at the current price, 0.5 is returned to shareholders.

Earning back entire market cap in 2 or 3 years is appealing.

```{code-cell} ipython3
import matplotlib.pyplot as plt
plt.plot([100, 80, 75, 76, 85])
```

Earning should be sustained for a bit.

Plot of expected earnings over the next few years based on article of expected phosphate rock.

<a href="https://www.statista.com/statistics/1251275/phosphate-rock-fertilizer-price-forecast/" rel="nofollow"><img src="https://www.statista.com/graphic/1/1251275/phosphate-rock-fertilizer-price-forecast.jpg" alt="Statistic: Price for phosphate rock from 2015 to 2020 with a forecast for 2021 to 2035 (in U.S. dollars per metric ton) | Statista" style="width: 100%; height: auto !important; max-width:1000px;-ms-interpolation-mode: bicubic;"/></a><br />Find more statistics at  <a href="https://www.statista.com" rel="nofollow">Statista</a>

```{code-cell}ipython3
import yfinance as yf
import mplfinance as mpf
sp = yf.Ticker("MBCF")
# Consider grabbing for valid date index instead
daily = sp.history(start="2016-01-02")
mpf.plot(daily,type='line')

last_year = sp.history(start="2021-03-14")
mpf.plot(last_year,type='candle',mav=(50, 100),volume=True)
```

Its a bit above the 50MA, want to wait until its below.

```{code-cell}ipython3
import numpy as np
def relative_strength(prices, n=14):
    """
    compute the n period relative strength indicator
    http://stockcharts.com/school/doku.php?id=chart_school:glossary_r#relativestrengthindex
    http://www.investopedia.com/terms/r/rsi.asp
    """
    deltas = np.diff(prices)
    seed = deltas[:n + 1]
    up = seed[seed >= 0].sum() / n
    down = -seed[seed < 0].sum() / n
    rs = up / down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100. / (1. + rs)

    for i in range(n, len(prices)):
        delta = deltas[i - 1]  # cause the diff is 1 shorter

        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up * (n - 1) + upval) / n
        down = (down * (n - 1) + downval) / n

        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)

    return rsi

for stock in ["ZIM", "DOLE", "SBSW"]
    zim = yf.Ticker(stock)
    zim = sp.history(start="2021-03-14")
    zim['rsi'] = relative_strength(zim['Close'],n=7)

    apd = mpf.make_addplot(zim['rsi'],panel=2,color='lime',ylim=(10,90),secondary_y=True)

    mpf.plot(zim,type='candle',volume=True,figscale=1.5,addplot=apd,panel_ratios=(1,0.6), title=f"{stock} - 2021-03-14")
```