import matplotlib.pyplot as plt
import pandas as pd

# numpy is the import Andy used to calc SD

spx = pd.read_csv("^spx_daily.csv", index_col="Date", parse_dates=True)
spx = spx[["Close"]]
spx['pctChange'] = spx["Close"].pct_change()
# eliminates "Close" column and only leaves pctChange in print view
spx = spx.drop("Close", axis=1)

values = spx['pctChange'].values
values = values[1:]

print(spx)


# Creates Histogram to graph 50 values # facecolor changes graph color #alpha changes transparency
plt.hist(values, 50, facecolor='red', alpha=0.7)

mean = spx['pctChange'].mean()
variance = spx['pctChange'].std()

# Plots the mean
# and different standard deviations using lines on graph
plt.axvline(x=mean)
# Within 6+/- standard deviations of mean sits 95.7% of data # At least it should - it didn't work for the banks in 2008 and fueled the crisis
plt.axvline(x=mean+3*variance)
plt.axvline(x=mean+4*variance)
plt.axvline(x=mean-3*variance)
plt.axvline(x=mean-4*variance)

plt.show()

# +=
