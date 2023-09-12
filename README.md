# Stock-Prediction-using-API

This Python script fetches stock data using the `yfinance` library and visualizes it using `matplotlib` and `mplfinance`.

## Requirements

- Python 3.6 or higher
- yfinance
- matplotlib
- mplfinance

You can install the required Python libraries using pip:


## Usage

Run the script in a Python environment. When prompted, enter your desired company's ticker symbol. The script will fetch the stock data for that company and display two plots: a line graph of the closing prices and a candlestick chart of the open-high-low-close (OHLC) data.


Please note that this script fetches data from Yahoo Finance via the `yfinance` library, which does not require an API key. If you're using a different API that does require an API key, you would need to modify the code to use that API.

## Disclaimer

This script is for educational purposes only and should not be used for making real-world investment decisions. The prediction model used in this script is very simple and is unlikely to give very accurate results. For more accurate predictions, you would need to use more sophisticated models and possibly more features (other than just the date).
