from twttr import shorten

def main():
    test_shorten()



def test_shorten():
    if shorten('Hello') == 'Hll':
        print('capital')

    # elif shorten("hello") == "hello":
    #     print('vowels not replaced')
    # if shorten("hello") == "hello":
    #     print('vowels not replaced')

if __name__ == "__main__":
    main()