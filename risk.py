import pandas as pd
import numpy as np
import pandas_datareader as pdr
import matplotlib.pyplot as plt

tikers = ['tqqq','aapl']

mydata = pd.DataFrame()

for t in tikers:
    mydata[t]= pdr.data.get_data_yahoo(t,start='2020-01-01')['Adj Close']

returns = np.log(mydata/mydata.shift(1)) # We used log returns.




print(returns[['aapl','tqqq']].mean() * 250 * 100)

'''
To calculate risk we use variance and standard devian. More deviation from the mean the more riskier the asset.
'''

print(returns[['aapl','tqqq']].var() * 250 ** 0.5 * 100) 

