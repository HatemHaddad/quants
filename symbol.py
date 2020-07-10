import pandas as pd
import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as plt

"""
This function reads a symbol and returns the stock from yahoo finance.
"""

def equity(symbol):
    stock = pdr.data.get_data_yahoo(symbol,start='2020-01-01')
    return stock

spy = equity('USO')

print(spy.info()) # Info about index, columns , ...

print(spy.shape) # Dataframe dimension

spy['Simple Returns'] = (spy['Adj Close']/spy['Adj Close'].shift(1))-1
print(spy['Simple Returns'])

spy['Simple Returns'].plot(figsize=(12,8))
#plt.show()

avg_return_d = spy['Simple Returns'].mean()

avg_return_a = avg_return_d * 250

print('Annual return : ' + str(round(avg_return_a,1)*100) + ' %')