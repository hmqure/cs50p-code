def main():
    frac = input("Fraction:")
    conv = convert(frac)
    print(gauge(conv))


def convert(fraction):
     n = 0
     try:
        split = fraction.split("/")
        n = n + (round(((int(split[0]))/(int(split[1])))*100))
        return n

    except ZeroDivisionError as e:
        pass

    except ValueError as e:
        pass



def gauge(percentage):

    if 1 < n < 99:
        return f"{str(n)}%"
        break

    elif n == 0 or n == 1:
        return "E"
        break

    elif n == 99 or n == 100:
        return "F"
        break

if __name__ == "__main__":
    main()