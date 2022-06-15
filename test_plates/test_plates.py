from plates import is_valid

def main():
    test_length()

def test_length():
    assert is_valid("G") return False
    # assert is_valid("AAAAAAAAAA") == "Invalid"
    # assert is_valid("HELLO") == "Valid"
    # assert is_valid("CS50") == "Valid"

if __name__ == "__main__":
    main()