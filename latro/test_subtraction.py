def subtract(a, b):
    return a-b


def test_subtract():
    assert subtract(1, 1) == 0
    assert subtract(0, 1) == -1
    assert subtract(0, -1) == 1
