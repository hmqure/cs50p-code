from plates import is_valid

def main():
    test_length()

def test_length():
    assert is_valid("G") == False
    assert is_valid("AAAAAAAAAA") == False
    assert is_valid("HELLO") == False
    assert is_valid("CS50") == False

if __name__ == "__main__":
    main()