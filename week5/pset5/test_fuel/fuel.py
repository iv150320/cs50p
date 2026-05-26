import sys


def main():
    s = input("Fraction: ")
    try:
        p = convert(s)
        print(gauge(p))
    except (ValueError, ZeroDivisionError):
        sys.exit(1)


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
