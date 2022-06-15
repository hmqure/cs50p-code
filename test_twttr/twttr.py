def main():
    enter = input("Input:")
    print(shorten(enter))

def shorten(word):

    new = ''
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(word)):
        if word[i] not in vowels:
            new += word[i]

    return new


if __name__ == "__main__":
    main()