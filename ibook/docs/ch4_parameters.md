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

(ch4_parameters)=
# Parameters

```{eval-rst}
.. table:: some_value_factors

    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                   Factor                    |                                                                                                                                                            Description                                                                                                                                                            |
    +=============================================+===================================================================================================================================================================================================================================================================================================================================+
    |Cash flow yield                              |The ratio divides the operational cash flow per share by the share price. A higher ratio implies better cash returns for shareholders (if paid out using dividends or share buybacks or profitably reinvested in the business).                                                                                                    |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Free cash flow yield                         |The ratio divides the free cash flow per share, which reflects the amount of cash available for distribution after necessary expenses and investments, by the share price. Higher and growing free cash flow yield is commonly viewed as a signal of outperformance.                                                               |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Cash flow return on invested capital (CFROIC)|CFROIC measures a company's cash flow profitability. It divides operating cash flow by invested capital, defined as total debt plus net assets. A higher return means the business has more cash for a given amount of invested capital, generating more value for shareholders.                                                   |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Cash flow to total assets                    |This ratio divides operational cash flow by total assets and indicates how much cash a company can generate relative to its assets, where a higher ratio is better, as with CFROIC.                                                                                                                                                |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Free cash flow to enterprise value           |This ratio measures the free cash flow that a company generates relative to its enterprise value, measured as the combined value of equity and debt. The debt and equity values can be taken from the balance sheet, but market values often provide a more accurate picture assuming the corresponding assets are actively traded.|
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |EBITDA to enterprise value                   |This ratio measures a company's earnings before interest, taxes, depreciation, and amortization (EBITDA), which is a proxy for cash flow relative to its enterprise value.                                                                                                                                                         |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Earnings yield                               |This ratio divides the sum of earnings for the past 12 months by the last market (close) price.                                                                                                                                                                                                                                    |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Earnings yield 1-year forward                |Instead of using historical earnings, this ratio divides the average of earnings forecasted by stock analyst for the next 12 months by the last price.                                                                                                                                                                             |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |PEG ratio                                    |The price/earnings to growth (PEG) ratio divides a stock's price-to-earnings  (P/E) ratio by the earnings growth rate for a given period. The ratio adjusts the price paid for a dollar of earnings (measured by the P/E ratio) by the company's earnings growth.                                                                  |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |P/E 1-year forward relative to the sector    |Forecasts the P/E ratio relative to the corresponding sector P/E. It aims to alleviate the sector bias of the generic P/E ratio by accounting for sector differences in valuation.                                                                                                                                                 |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Sales yield                                  |The ratio measures the valuation of a stock relative to its ability to generate revenues. All else being equal, stocks with higher historical sales to price ratios are expected to outperform.                                                                                                                                    |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Sales yield forward                          |The forward sales-to-price ratio uses analyst sales forecast, combined to a (weighted) average.                                                                                                                                                                                                                                    |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Book value yield                             |The ratio divides the historical book value by the share price.                                                                                                                                                                                                                                                                    |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |Dividend yield                               |The current annualized dividend divided by the last close price. Discounted cash flow valuation assumes a company's market value equates to the present value of its future cash flows.                                                                                                                                            |
    +---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

Other important terms include {term}`DeadCatBounce`.

In addition there are certain quality factors that indicate a company will perform well. For example, they are cash flow positive and no longer need to dilute shareholder value by selling sells. This may indicate they have low finance risk and will not go bankrupt.

|Factor                |Description                                                                                                                             |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|Asset turnover        |This factor measures how efficiently a company uses its assets, which require capital, to produce revenue and is calculated by dividing sales by total assets. A higher turnover is better.|
|Asset turnover 12-month change|This factor measures a change in management's efficiency in using assets to produce revenue over the last year. Stocks with the highest level of efficiency improvements are typically expected to outperform.|
|Current ratio         |The current ratio is a liquidity metric that measures a company's ability to pay short-term obligations. It compares a company's current assets to its current liabilities, and a higher current ratio is better from a quality perspective.|
|Interest coverage     |This factor measures how easily a company will be able to pay interest on its debt. It is calculated by dividing a company's earnings before interest and taxes (EBIT) by its interest expense. A higher ratio is desirable.|
|Leverage              |A firm with significantly more debt than equity is considered to be highly leveraged. The debt-to-equity ratio is typically inversely related to prospects, with lower leverage being better.|
|Payout ratio          |The share of earnings paid out in dividends to shareholders. Stocks with higher payout ratios are ranked higher.                        |
|Return on equity (ROE)|ROE is computed as the ratio of net income to shareholders' equity. Equities with higher historical returns on equity are ranked higher.|

Terms explained

What Is the Current Ratio?
The current ratio is a liquidity ratio that measures a company’s ability to pay short-term obligations or those due within one year. 
$$
  Debt / Equity = \frac{Total Liabilities}{Total Shareholder's Equity}
$$

A ratio under 1.00 indicates that the company’s debts due in a year or less are greater than its assets—cash or other short-term assets expected to be converted to cash within a year or less. A current ratio of less than 1.00 may seem alarming, although different situations can negatively affect the current ratio in a solid company.

A high D/E ratio is often associated with high risk; it means that a company has been aggressive in financing its growth with debt.
