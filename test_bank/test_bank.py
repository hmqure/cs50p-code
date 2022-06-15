from bank import value

def main():
    test_value()

def test_value():
    assert value("Hello") == "$0"
    assert value("hello") == "$0"
    assert value("hey") == "$20"
    assert value("Hopper") == "$20"
    assert value("Hello") == "$0"
    assert value("Hello") == "$0"



if __name__ == "__main__":
    main()