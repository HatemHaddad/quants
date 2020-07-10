import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt

tickers = ['MSFT','AAPL','TQQQ']

mydata = pd.DataFrame()

for t in tickers:
  mydata[t] = pdr.data.get_data_yahoo(t, start='2020-01-01')['Adj Close']
  
print(mydata)


(mydata/mydata.iloc[0]*100).plot(figsize=(12,8))
plt.show()
