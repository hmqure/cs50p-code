from fuel import convert, gauge
import sys

def main():
    test_convert()
    test_gauge()
    test_zero()
    test_value()


def test_convert():

    assert convert('2/3') == 67
    assert convert('4/5') == 80


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert('2/0')


def test_value():
    with pytest.raises(ValueError):
        convert('cat/dog')


def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(1) == 'E'
    assert gauge(67) == '67%'

if __name__ == "__main__":
    main()