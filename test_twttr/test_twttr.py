from twttr import shorten

def main():
    test_shorten()



def test_shorten():
    if shorten("hello") != "hll:
        print('Error')



if __name__ == "__main__":
    main()