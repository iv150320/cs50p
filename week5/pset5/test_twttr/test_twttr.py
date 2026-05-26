from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"


def test_mixed():
    assert shorten("Twitter") == "Twttr"


def test_no_vowels():
    assert shorten("bcdf") == "bcdf"
    assert shorten("rhythm") == "rhythm"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"
