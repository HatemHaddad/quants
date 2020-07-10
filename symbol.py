import pandas as pd
import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as pls

"""
This function reads a symbol and returns the stock from yahoo finance.
"""

def equity(symbol):
    stock = pdr.data.get_data_yahoo(symbol,start='2020-01-01')
    return stock

spy = equity('PG')

print(spy.info()) # Info about index, columns , ...

print(spy.shape) # Dataframe dimension

print("Hello")
