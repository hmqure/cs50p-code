import random


def main():
    lev = get_level()
    counter = 0
    wrong = 0
    start = 10
    incorrect = 0

    while True:
        expr = generate_integer(lev)
        if counter < 10:
            while True:
                if wrong != 3:
                    ans = input(f"{expr[0]} + {expr[1]} = ")
                    if int(ans) == (expr[0] + expr[1]):
                        counter = counter + 1
                        break
                    elif int(ans) != (expr[0] + expr[1]):
                        if wrong != 3:
                            print('EEE')
                            wrong = wrong + 1
                            pass
                elif wrong == 3:
                    print((f"{expr[0]} + {expr[1]} = "),expr[0]+expr[1])
                    wrong = wrong - wrong
                    incorrect = incorrect + 1
                    break

        elif counter == 10:
            print(start-incorrect)
            break



def get_level():

    num = [1,2,3]

    while True:
        try:
            level = input("Level:")
            if int(level) in num:
                return int(level)
                break
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):

    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        return [x, y]

    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return [x, y]

    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return [x, y]



if __name__ == "__main__":
    main()