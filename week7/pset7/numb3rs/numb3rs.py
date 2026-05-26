import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if match:
        for g in match.groups():
            if int(g) < 0 or int(g) > 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
