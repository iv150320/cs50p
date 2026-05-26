# Stock Portfolio Tracker

#### Video Demo: https://youtu.be/EXAMPLE

#### Description:

The Stock Portfolio Tracker is a command-line application that allows users to manage a virtual stock portfolio and fetch real-time stock data. It uses the `yfinance` library to pull current market data from Yahoo Finance without requiring an API key.

The program presents a simple text menu with five options:

1. **Add stock** — Enter a ticker symbol (e.g., AAPL) and number of shares to add to your portfolio. If the stock already exists, the shares are added to the existing position.
2. **Remove stock** — Remove some or all shares of a stock from your portfolio.
3. **View portfolio** — Display a formatted table of all holdings with current prices, individual position values, daily change, and a total portfolio value.
4. **Check single stock price** — Look up the current price, daily change, and percentage change for any ticker without adding it to the portfolio.
5. **Exit** — Quit the program.

The project consists of the following files:

- **project.py** — The main program file containing:
  - `main()` — The entry point that runs the interactive CLI loop.
  - `get_stock_data(ticker)` — Fetches current price, daily change, and percentage change for a given ticker using yfinance. Returns a dict or None on failure.
  - `calculate_value(price, shares)` — Computes the total dollar value of a position. Returns price × shares as a float.
  - `format_portfolio(portfolio)` — Takes a dictionary of ticker→shares and returns a formatted string table with current prices and values for all holdings.

- **test_project.py** — Contains pytest tests for all three custom functions:
  - `test_calculate_value()` — Verifies basic multiplication, zero shares, zero price, and float precision.
  - `test_get_stock_data_success()` — Mocks yfinance to test that price, change, and change_pct are computed correctly.
  - `test_get_stock_data_no_price()` — Tests handling of tickers with no available price data.
  - `test_get_stock_data_exception()` — Tests graceful handling of API exceptions.
  - `test_format_portfolio()` — Mocks `get_stock_data` to verify the portfolio table renders correctly.

- **requirements.txt** — Lists the Python dependencies: `yfinance` for market data and `pytest` for testing.
