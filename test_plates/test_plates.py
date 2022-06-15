from plates import is_valid

def main():
    test_len()

def test_len():
    assert is_valid("G") is not True
    assert is_valid("AAAAAAAAAA") is not True
    assert is_valid("HELLO") is True
    assert is_valid("CS50") is True

if __name__ == "__main__":
    main()