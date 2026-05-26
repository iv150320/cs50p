import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    price = r.json()["bitcoin"]["usd"]
except requests.RequestException:
    sys.exit("Could not fetch Bitcoin price")

print(f"${n * price:,.4f}")
