amount_due = 50
while amount_due > 0:
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        amount_due -= coin
    if amount_due > 0:
        print(f"Amount Due: {amount_due}")
print(f"Change Owed: {abs(amount_due)}")
