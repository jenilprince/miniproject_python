##THIS IS NOT ACCURATE

import yfinance as yf
from sklearn.linear_model import LinearRegression
import datetime
import pandas as pd
import warnings
warnings.filterwarnings('ignore', message='X has feature names')
import numpy as np
#Stock symbol and dates
stock_symbol = 'LT.NS'
start_date="2004-07-28"
end_date=datetime.date.today().strftime("%Y-%m-%d")
#download stock data
data=yf.download(stock_symbol,start=start_date,end=end_date,auto_adjust=True)
#clean nd prepare data
data=data[['Close']].dropna()
data.reset_index(inplace=True)
data['Day']=data.index

X=data[['Day']]
y=data['Close']

model=LinearRegression()
model.fit(X,y)
#Current price
stock =yf.Ticker(stock_symbol)
current=stock.history(period='1d')['Close'].iloc[-1]
print(f"Current price of {stock_symbol}: ₹{current:.4f}")

#Predict future
future_days=int(input("Enter the number of days to predict: "))
future=pd.DataFrame({'Day': list(range(len(data),len(data)+future_days))})
predicted_prices=model.predict(future)
print(f"{predicted_prices[:]}")


