def main():
    ...


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


if __name__ == "__main__":
    main()