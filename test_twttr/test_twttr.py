from twttr import shorten

def main():
    test_shorten()



def test_shorten():
    assert shorten('hello') == 'hll'
    assert shorten('Hello') == 'Hll'
    assert shorten('HELLO') == 'HLL'
    assert shorten('123') == '123'
    assert shorten('hello123') == 'hll123'
    assert shorten('hello, world') == 'hll, wrld'

if __name__ == "__main__":
    main()