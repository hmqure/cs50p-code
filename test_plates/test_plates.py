from plates import is_valid

def main():
    test_len()
    test_alph()
    test_zero()
    test_alnum()

def test_len():
    assert is_valid("G") is not True
    assert is_valid("AAAAAAAAAA") is not True
    assert is_valid("HELLO") is True
    assert is_valid("CS50") is True

def test_alph():
    assert is_valid('2AAAA') is not True
    assert is_valid('AAA22A') is not True
    assert is_valid('AAA222') is True

def test_zero():
    assert is_valid('AAA022') is not True

def test_alnum():
    assert is_valid('AAA./2') is not True


if __name__ == "__main__":
    main()