months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
while True:
    s = input("Date: ")
    try:
        if "/" in s:
            m, d, y = s.split("/")
            m, d, y = int(m), int(d), int(y)
        elif "," in s:
            s = s.replace(",", "")
            m, d, y = s.split(" ")
            m = months.index(m) + 1
            m, d, y = int(m), int(d), int(y)
        else:
            continue
        if m < 1 or m > 12 or d < 1 or d > 31:
            continue
        print(f"{y:04}-{m:02}-{d:02}")
        break
    except (ValueError, IndexError):
        continue
