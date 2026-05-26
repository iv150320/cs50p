def main():
    s = input("Input: ")
    print(shorten(s))


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for c in word:
        if c not in vowels:
            result += c
    return result


if __name__ == "__main__":
    main()
