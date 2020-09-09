import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf

vst = yf.Ticker("VST.CN")
data = vst.history(interval="1d", start_date="08-08-2020", end_date="09-08-2020")
mpf.plot(
    data,
    type="candle",
    savefig="vst_purchases.png",
    mav=4,
    title="Victory Square Purchases Dates",
    vlines=dict(
        vlines=["08-26-2020", "09-03-2020", "09-08-2020"], linewidths=(0.5, 0.5, 0.5)
    ),
)
