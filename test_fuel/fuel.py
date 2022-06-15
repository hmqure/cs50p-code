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
            return e

        except ValueError as e:
            return e



def gauge(n):

    try:
        if 1 < n < 99:
            return f"{str(n)}%"

        elif n == 0 or n == 1:
            return "E"


        elif n == 99 or n == 100:
            return "F"
    except:
        if n > 100:
            return ValueError()



if __name__ == "__main__":
    main()