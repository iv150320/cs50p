while True:
    s = input("Fraction: ")
    try:
        x, y = s.split("/")
        x, y = int(x), int(y)
        if y == 0 or x > y:
            raise ValueError
        p = round(x / y * 100)
    except (ValueError, ZeroDivisionError):
        continue
    if p <= 1:
        print("E")
    elif p >= 99:
        print("F")
    else:
        print(f"{p}%")
    break
