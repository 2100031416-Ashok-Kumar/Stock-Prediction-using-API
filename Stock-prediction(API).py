import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns

def fetch_historical_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    data = data.drop('Adj Close', axis=1)
    data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    return data

def fetch_live_data(ticker):
    live_data = yf.download(ticker, period='1d', interval='1m')
    live_data = live_data.drop('Adj Close', axis=1)
    live_data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    return live_data

def plot_linear_regression(data, ticker):
    data['Date'] = data.index
    data['Date_ordinal'] = pd.to_datetime(data['Date']).map(pd.Timestamp.toordinal)
    
    X = data['Date_ordinal'].values.reshape(-1, 1)
    Y = data['Close'].values.reshape(-1, 1)
    model = LinearRegression().fit(X, Y)
    
    future_dates = pd.date_range(start=data.index[-1], periods=30, freq='D')
    future_dates_ordinal = pd.to_datetime(future_dates).map(pd.Timestamp.toordinal)
    future_predictions = model.predict(np.array(future_dates_ordinal).reshape(-1, 1))
    
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Close'], label='Historical Prices')
    plt.plot(future_dates, future_predictions, label='Linear Regression Prediction', linestyle='--')
    plt.title(f'{ticker} Stock Price with Linear Regression')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

def percentage_increase(data):
    data['Percentage Increase'] = ((data['Close'] - data['Close'].shift(1)) / data['Close'].shift(1)) * 100
    return data

def scatter_plot_matrix(data):
    sns.pairplot(data.dropna())
    plt.show()

def main():
    api_key = input("Please enter your API key: ") 
    ticker = input("Please enter the company's ticker symbol: ")
    
    start_date = '2020-01-01'
    end_date = '2022-12-31'
    historical_data = fetch_historical_data(ticker, start_date, end_date)
    
    historical_data['Close'].plot(title=f'{ticker} Stock Price')
    plt.show()
    
    mpf.plot(historical_data, type='candle', mav=(3, 6, 9), volume=True, title=f'{ticker} OHLC Data', warn_too_much_data=len(historical_data) + 100)
    
    plot_linear_regression(historical_data, ticker)
    
    percentage_data = percentage_increase(historical_data)
    
    scatter_plot_matrix(percentage_data)
    
    try:
        while True:
            live_data = fetch_live_data(ticker)
            
            plot_linear_regression(live_data, ticker)
            mpf.plot(live_data, type='candle', mav=(3, 6, 9), volume=True, title=f'{ticker} Live OHLC Data', warn_too_much_data=len(live_data) + 100)
            time.sleep(60)
    except KeyboardInterrupt:
        print("Live update stopped.")

if __name__ == "__main__":
    main()
