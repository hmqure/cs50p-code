from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()



def test_convert():
    assert convert('hello') == 'hll'
    assert shorten('Hello') == 'Hll'
    assert shorten('HELLO') == 'HLL'

def test_gauge():
    assert shorten('hello') == 'hll'
    assert shorten('Hello') == 'Hll'

if __name__ == "__main__":
    main()