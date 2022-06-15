from plates import is_valid

def main():
    test_length()

def test_length():
    assert is_valid("G") is False
    assert is_valid("AAAAAAAAAA") is False
    assert is_valid("HELLO") is False
    assert is_valid("CS50") is False

if __name__ == "__main__":
    main()