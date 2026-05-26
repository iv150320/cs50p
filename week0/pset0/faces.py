def main():
    s = input()
    print(convert(s))


def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s


main()
