from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello there") == 0
    assert value("Hello, Newman") == 0


def test_h():
    assert value("how you doing?") == 20
    assert value("Hey") == 20
    assert value("hi") == 20


def test_other():
    assert value("what's happening?") == 100
    assert value("good morning") == 100
    assert value("") == 100


def test_case():
    assert value("HELLO") == 0
    assert value("HOW") == 20
