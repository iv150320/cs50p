from plates import is_valid


def test_length():
    assert is_valid("H") == False
    assert is_valid("HE") == True
    assert is_valid("HELLO") == True
    assert is_valid("HELLOCS") == False


def test_start():
    assert is_valid("50") == False
    assert is_valid("A5") == False
    assert is_valid("AB") == True


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("AAA222") == True


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("HELLO ") == False
    assert is_valid("CS 50") == False


def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("ABC0") == False
