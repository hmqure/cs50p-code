from fuel import convert, gauge
import sys

def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert('2/3') == 67

    try:
        assert convert('4/5') == 80

    except ValueError:
        
   # assert convert('2/0') is SystemExit


def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(1) == 'E'
    assert gauge(67) == '67%'

if __name__ == "__main__":
    main()