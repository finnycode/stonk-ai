from os import read
import numpy as np
import pandas as pd
import yfinance as yf
import time as t
import matplotlib.pyplot as plt
from sklearn import linear_model
import requests
import csv
from io import StringIO
import requests
from datetime import datetime

tickerinput = input('Ticker: ')
data = yf.download(tickers=tickerinput, period='5d', interval="1m")
openprice=data['Open']
high=data['High']
low=data['Low']
close=data['Close']
ticker_data = yf.Ticker(tickerinput).history("1m")

csv_link = 'https://query1.finance.yahoo.com/v7/finance/download/' + tickerinput.upper() + '?period1=-252374400&period2=1621987200&interval=1d&events=history&includeAdjustedClose=true'

req = requests.get(csv_link)

url_content = req.content
csv_file = open('bruh.csv', 'wb')
csv_file.write(url_content)
csv_file.close()

    
raw_data = pd.read_csv('bruh.csv')
print(raw_data)

    
csv_data = csv_file








High=pd.DataFrame(raw_data['High'])
Low=pd.DataFrame(raw_data['Low'])
lm = linear_model.LinearRegression()
model = lm.fit(High, Low)
new_high = ticker_data['High']
new_low = ticker_data['Low']

High_new=np.array([new_high])
Low_new=np.array([new_low])
High_new = High_new.reshape(-1,1)
Low_new = Low_new.reshape(-1,1)
High_predict=model.predict(High_new)
Low_predict=model.predict(Low_new)
print(High_predict)
print(Low_predict)

data.plot(kind='scatter', x='High', y='Low')
plt.plot(High,model.predict(High),color='red', linewidth=2)
plt.scatter(High_new, Low_predict, color='red')
plt.scatter(Low_new, High_predict, color='green')