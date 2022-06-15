import sys

def main():
    frac = input("Fraction:")
    conv = convert(frac)
    print(gauge(conv))


def convert(fraction):

    while True:
        n = 0
        try:
            split = fraction.split("/")
            n = n + (round(((int(split[0]))/(int(split[1])))*100))
            return n

        except ZeroDivisionError as e:
            sys.exit()

        except ValueError as e:
            sys.exit()



def gauge(n):

    if 1 < n < 99:
        return f"{str(n)}%"

    elif n == 0 or n == 1:
        return "E"


    elif n == 99 or n == 100:
        return "F"


if __name__ == "__main__":
    main()