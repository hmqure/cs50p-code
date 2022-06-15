from bank import value

def main():
    test_hello()
    test_h()
    test_non()

def test_hello():
    assert value("") == 0
    assert value("hello") == 0

def test_h():
    assert value("hey") == 20
    assert value("Hopper") == 20

def test_non():
    assert value("very") == 100
    assert value("3453") == 100
    assert value("?>/.") == 100

if __name__ == "__main__":
    main()