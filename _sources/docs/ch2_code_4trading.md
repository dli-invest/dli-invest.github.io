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

(pd_functions)=
# Code For Trading

Pandas is an excellent library for analyzing and dealing with data.

In order to calculate profits and how much money to I put into the market, I use a formula after downloading my data from RBC direct investing.

```{code-cell} ipython3
import pandas as pd
data = {
    "Activity": {
        0: "Buy",
        1: "Buy",
        2: "Deposits & Contributions",
        3: "Withdrawals & De-registrations",
        4: "Deposits & Contributions",
    },
    "Symbol": {0: "BB", 1: "RBF556", 2: "", 3: "RBF558", 4: ""},
    "Value": {0: -100.95, 1: -2328.24, 2: 1000.0, 3: -14000.0, 4: 15000.0},
}
df = pd.DataFrame.from_dict(data)

print(df)

deposit_df = df[df.Activity == "Deposits & Contributions"]
divid_df = df[df.Activity == "Dividends"]
with_df = df[df.Activity == "Withdrawals & De-registrations"]
total = deposit_df['Value'].sum() + with_df['Value'].sum()
print(total)
```

% Continue on with pandas examples