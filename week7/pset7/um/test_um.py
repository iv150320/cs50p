from um import count


def test_single():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1


def test_multiple():
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3


def test_not_word():
    assert count("yummy") == 0
    assert count("instrument") == 0
    assert count("circumstance") == 0
    assert count("") == 0
