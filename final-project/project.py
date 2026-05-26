import yfinance as yf
import sys


def main():
    portfolio = {}
    while True:
        print("\n=== Stock Portfolio Tracker ===")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. View portfolio")
        print("4. Check single stock price")
        print("5. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            ticker = input("Ticker: ").strip().upper()
            try:
                shares = int(input("Shares: "))
            except ValueError:
                print("Invalid number of shares")
                continue
            portfolio[ticker] = portfolio.get(ticker, 0) + shares
            print(f"Added {shares} shares of {ticker}")
        elif choice == "2":
            ticker = input("Ticker: ").strip().upper()
            if ticker in portfolio:
                try:
                    shares = int(input("Shares to remove: "))
                except ValueError:
                    print("Invalid number")
                    continue
                portfolio[ticker] -= shares
                if portfolio[ticker] <= 0:
                    del portfolio[ticker]
                print(f"Removed {shares} shares of {ticker}")
            else:
                print(f"{ticker} not in portfolio")
        elif choice == "3":
            if not portfolio:
                print("Portfolio is empty")
            else:
                print(format_portfolio(portfolio))
        elif choice == "4":
            ticker = input("Ticker: ").strip().upper()
            data = get_stock_data(ticker)
            if data:
                print(f"{ticker}: ${data['price']:.2f} ({data['change']:+.2f}, {data['change_pct']:+.2f}%)")
            else:
                print(f"Could not fetch data for {ticker}")
        elif choice == "5":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice")


def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        price = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")
        if price is None:
            return None
        prev_close = info.get("previousClose") or price
        change = price - prev_close
        change_pct = (change / prev_close) * 100 if prev_close else 0
        return {"price": price, "change": change, "change_pct": change_pct}
    except Exception:
        return None


def calculate_value(price, shares):
    return price * shares


def format_portfolio(portfolio):
    lines = []
    lines.append(f"{'Ticker':<8} {'Shares':<8} {'Price':<10} {'Value':<12} {'Change':<10}")
    lines.append("-" * 50)
    total = 0
    for ticker in sorted(portfolio):
        shares = portfolio[ticker]
        data = get_stock_data(ticker)
        if data:
            price = data["price"]
            value = calculate_value(price, shares)
            total += value
            lines.append(f"{ticker:<8} {shares:<8} ${price:<8.2f} ${value:<10.2f} {data['change']:+.2f}")
        else:
            lines.append(f"{ticker:<8} {shares:<8} ?")
    lines.append("-" * 50)
    lines.append(f"{'Total':<39} ${total:<.2f}")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
