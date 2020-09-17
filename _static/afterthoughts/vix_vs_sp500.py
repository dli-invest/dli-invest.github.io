# download files for S&P 500 plot
# http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv
import pandas as pd
import io
import requests
import yfinance as yf
import mplfinance as mpf

# data is only up to 2004
url = "http://www.cboe.com/publish/scheduledtask/mktdata/datahouse/vixcurrent.csv"
s = requests.get(url).content
vix = pd.read_csv(io.StringIO(s.decode("utf-8")))
# VIX Open,VIX High,VIX Low,VIX Close
vix = vix.iloc[
    1:,
]
vix.columns = ["Date", "Open", "High", "Low", "Close"]
vix["Date"] = pd.to_datetime(vix["Date"].astype(str), format="%m/%d/%Y")
# vix.rename(columns={"VIX Open": "Open", "VIX High": "High", "VIX Close": "Close"})
vix[["Open", "High", "Close"]] = vix[["Open", "High", "Close"]].apply(pd.to_numeric)
vix = vix.set_index("Date", drop=True)
vix.to_csv("vix_curr.csv", index=True)

sp = yf.Ticker("^GSPC")
# Consider grabbing for valid date index instead
history = sp.history(start="2004-01-02")
apds = [
    mpf.make_addplot(vix.Open.values, linestyle="dotted", ylabel="Volality VIX (Open)"),
]

fig, axes = mpf.plot(
    history,
    addplot=apds,
    ylabel="Price (USD)",
    returnfig=True,
    figscale=1.2,
    title="S&P 500",
)

axes[0].legend(["S&P500", "VIX"], loc="upper left")
fig.savefig("vix_vs_s&p500.png")
