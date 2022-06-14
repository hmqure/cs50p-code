from twttr import shorten
import sys

def main():
    test_shorten()



def test_shorten():

    if shorten("Hello") == "Hll":
        sys.exit

    if shorten("hello") == 'hello':
        sys.exit


    # elif shorten("hello") == "hello":
    #     print('vowels not replaced')
    # if shorten("hello") == "hello":
    #     print('vowels not replaced')





if __name__ == "__main__":
    main()