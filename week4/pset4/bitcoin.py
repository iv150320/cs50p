import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=ReplaceWithYourCoinCapAPIKey")
    r.raise_for_status()
    data = r.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Could not fetch Bitcoin price")

print(f"${n * price:,.4f}")
