items = {}
while True:
    try:
        item = input().lower()
    except EOFError:
        print()
        break
    if item in items:
        items[item] += 1
    else:
        items[item] = 1
for item in sorted(items):
    print(items[item], item.upper())
