import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datetime import datetime,timedelta
import numpy as np
import operator
import itertools
import asyncio
import json
import csv
from binance import AsyncClient, DepthCacheManager, BinanceSocketManager
from binance import Client
import config
client = Client(config.api_key, config.api_secret)


#klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "4 years ago UTC")
#with open('data.csv', 'w', newline='') as csvfile:
    #datawriter = csv.writer(csvfile)
    #datawriter.writerow(['timestamp open','o','h','l','c','Volume','Close time','asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','Can be ignored'])
    #for x in klines:
       #datawriter.writerow(x)
df=pd.read_csv('data.csv')

df['difference']=abs(df['o']-df['c'])
print(df['difference'].head)
print(df['Number of trades'].head)
ax1 = df.plot.scatter(x='Volume',
                      y='Number of trades',
                      c='DarkBlue')
r = np.corrcoef(df['Volume'], df['Number of trades'])
print(r)
plt.show()
plt.close()
ax1 = df.plot.scatter(x='Volume',
                      y='difference',
                      c='DarkBlue')
plt.show()
r = np.corrcoef(df['Volume'], df['difference'])
print(r)
