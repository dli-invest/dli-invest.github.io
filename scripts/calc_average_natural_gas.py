# calculate average from daily data from natural gas futures from yahoo finance
import yfinance
import pandas as pd

# read NG=F 2 years worth of data

nat_gas = yfinance.download("NG=F", start="2021-01-01", end="2023-01-01")

nat_gas['Month'] = pd.to_datetime(nat_gas.index)
# pad all date
# print(nat_gas.groupby(by=['Volume', 'Adj Close', pd.Grouper(key='Month', freq='3M')])['Open'].agg('mean'))

mths_3 = pd.date_range(end = nat_gas.index[-1], freq=pd.offsets.BQuarterEnd(),periods=8)
# mths_6 = pd.date_range(end = nat_gas.index[-1], freq=pd.offsets.MonthBegin(6),periods=4)

mth3 = (nat_gas
         #filter for last three months
        .loc[mths_3]
        .groupby(["Month", "Volume"])
        .agg(avg_ng_last_3_months=("Open","mean"))
        )

# mth6 = (nat_gas
#          #filter for last six months
#         .loc[mths_6]
#          .groupby(["Volume", "Month"])
#         .agg(avg_invoices_last_6_months=("Open","mean"))
#         )

print(mth3)

# random guess from last two quarters of profit
# at 4.558 assume 360 revenue for Q4 and 160M profit
# 475 revenue and 260M profit for Q4
# considering the investor presentation, thinking its closer to 360M revenue and 160 M profit.
quarterly_profit = 160
# 	266.05M * 0.2
# if deliveries are 3 quarters behind then 


quarterly_dividend = 266.05 * 0.2
print(quarterly_dividend)

remaining_revenue = quarterly_profit - quarterly_dividend
print(remaining_revenue)
# 176 debt
total_debt = 176

# max debt reduction (they target to get to 50M USD in debt)
min_debt_reduction = total_debt - 100

print(min_debt_reduction)
# bunch of risk of falling gas prices, but with new supply reduction from russia, doubt it would be so bad.