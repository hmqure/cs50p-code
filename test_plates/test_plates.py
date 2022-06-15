from plates import is_valid

def main():
    is_valid()

def test_length():
    assert is_valid("G") == "Invalid"
    assert is_valid("AAAAAAAAAA") == "Invalid"
    assert is_valid("HELLO") == "Invalid"
    assert is_valid("CS50") == "Invalid"

if __name__ == "__main__":
    main()