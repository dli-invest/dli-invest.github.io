## investing Book

This book contains information on my investing best practises as well as what I will do in the future for my investments. This is all my opinion and its really hard to say what the market will do in the future.


### Overview



To publish


Build sphinx files

```
jb build ibook/
```

```
jupytext CorrelationExamples.ipynb --to rmarkdown
```

* Risk of Returns
* Price Prediction (Practically useless for what I buy)
* Online Portoflio Selection (Just for Verification/Validation)
* Estimation of Returns

New Risk Page will be made for risk management per tag with useless price predictions
Periodic publishing for online portoflio selection and risk management for current portfolio.


#### TodoList

**06/13/2020**

* add more examples

**06/07/2020**
* ~~Limit to 2 decimals make columns 6 instead of 3~~
* Append data to hardcoded csv (won't do, stocks will change too quickly)

#### SubReports

Github Pages with Specific Folder Report on Risk.
Generate risk with different holdings, append to different csvs based on settings.
Complex config.yml file?


**Disclaimer** Major non day trade purchases will be recorded here.

Note this will not be rolling, say I buy a stock
```
risk:
  -  stocks:
     weights:
     output_csv:
  -  stocks:
     weights:
     output_csv:
```

Then my logic will iterate across tickers in the csv and generate images for them.

##### References


https://mlfinlab.readthedocs.io/en/latest/portfolio_optimisation/risk_metrics.html

