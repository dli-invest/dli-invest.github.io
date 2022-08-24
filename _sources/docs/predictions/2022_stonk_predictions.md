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