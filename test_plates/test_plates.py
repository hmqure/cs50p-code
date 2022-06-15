from plates import is_valid

def main():
    test_length()

def test_length():
    assert is_valid("G") == "Invalid"
    assert value("AAAAAAAAAA") == "Invalid"
    assert value("HELLO") == "Invalid"
    assert value("CS50") == "Invalid"

if __name__ == "__main__":
    main()