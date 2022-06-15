from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()



def test_convert():
    assert convert('2/3') == 67
    assert convert('2/0') raise ZeroDivisionError


def test_gauge():
    assert gauge(100) == 'F'
    assert gauge(1) == 'E'
    assert gauge(67) == '67%'

if __name__ == "__main__":
    main()