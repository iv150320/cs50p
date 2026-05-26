from datetime import date
import sys
import inflect


def main():
    birth = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date")
    minutes = date_diff_minutes(birth_date, date.today())
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    print(words.capitalize(), "minutes")


def date_diff_minutes(d1, d2):
    delta = d2 - d1
    return delta.days * 24 * 60


if __name__ == "__main__":
    main()
