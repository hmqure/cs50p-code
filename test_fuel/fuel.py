def main():
    ...


def convert(fraction):
     n = 0
     try:
        split = frac.split("/")
        n = n + (round(((int(split[0]))/(int(split[1])))))
        return n

    except ZeroDivisionError as e:
        pass

    except ValueError as e:
        pass


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()