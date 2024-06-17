import yfinance as yf
import matplotlib.pyplot as plt

def plot_stock_price(ticker):
    try:
        # Fetch historical data using yfinance
        ticker_data = yf.Ticker(ticker)
        hist = ticker_data.history(period="1y")
        
        # Plotting with matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(hist.index, hist['Close'], marker='o', linestyle='-', color='b', label=f'{ticker} Closing Price')
        plt.title(f'Stock Price Chart for {ticker}')
        plt.xlabel('Date')
        plt.ylabel('Price ($)')
        plt.grid(True)
        plt.legend()
        
        # Saving the plot as an image
        plt.savefig('stock_chart.png')
        
        # Displaying the plot or sending it somewhere (in a Discord bot, for example)
        # You can send the image to Discord or display it in a web application
        
        plt.show()  # If you are running this in a Jupyter notebook or locally
        
    except Exception as e:
        print(f"Error plotting stock price for {ticker}: {e}")

# Example usage:
ticker = 'V'  # Example ticker symbol (Apple Inc.)
plot_stock_price(ticker)
