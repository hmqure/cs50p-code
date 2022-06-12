while True:
    frac = input("Fraction:")
    n = 0
    try:
        split = frac.split("/")
        n = n + (round(((int(split[0]))/(int(split[1])))*100))

        if 1 < n < 99:
            print(str(n)+"%")
            break

        elif n == 0 or n == 1:
            print("E")
            break

        elif n == 99 or n == 100:
            print("F")
            break

        elif n > 100:
            pass

    except ZeroDivisionError as e:
        pass

    except ValueError as e:
        pass

    