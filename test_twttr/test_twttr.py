from twttr import shorten

def main():
    test_shorten()



def test_capital():

    if shorten("hello") == "hello":
        print('vowels not replaced')

    if shorten("Hello") == "Hll":
        print('vowels not replaced')

    if shorten("hEllo") == "hEllo":
        print('vowels not replaced')

if __name__ == "__main__":
    main()