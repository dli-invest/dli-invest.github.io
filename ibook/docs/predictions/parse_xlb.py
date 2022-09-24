import pandas as pd 

df = pd.read_csv("xsb_holdings.csv")

# find columns with Duration less than 2 years and coupon less than 1.5%
df = df[(df["Duration"] < 2.74)]

print(df)

# total weight

print(df["Weight (%)"].sum())
print(df["Coupon (%)"].mean())
coupon_low = df[(df["Coupon (%)"] < 3.5)]
print(coupon_low["Coupon (%)"].mean())
print(coupon_low["Weight (%)"].sum())