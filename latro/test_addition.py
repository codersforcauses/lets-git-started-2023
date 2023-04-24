def addition(a,b):
    return a+b

def test_addition():
    assert addition(1, 1) == 2
    assert addition(0, 1) == 1
    assert addition(0, -1) == -1