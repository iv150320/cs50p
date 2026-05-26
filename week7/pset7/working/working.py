import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError
    h1, m1, p1, h2, m2, p2 = match.groups()
    m1 = m1 or "00"
    m2 = m2 or "00"
    h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)
    if not (1 <= h1 <= 12) or not (1 <= h2 <= 12) or not (0 <= m1 <= 59) or not (0 <= m2 <= 59):
        raise ValueError
    if p1 == "AM":
        h1 = 0 if h1 == 12 else h1
    else:
        h1 = 12 if h1 == 12 else h1 + 12
    if p2 == "AM":
        h2 = 0 if h2 == 12 else h2
    else:
        h2 = 12 if h2 == 12 else h2 + 12
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()
