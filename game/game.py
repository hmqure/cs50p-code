import random

counter = 0

while counter == 0:

    level = input("Level:")

    if level.isdigit() is True:

        if int(level) >= 1:
            print(level)

            while True:

                guess = input("Guess:")
                num = random.randint(1,int(level))

                if guess.isdigit() is True:

                    if int(guess) == num:
                        print('Just right!')
                        counter = counter + 1
                        break

                    elif int(guess) > num:
                        print("Too large!")
                        pass

                    elif int(guess) < num:
                        print("Too small!")
                        pass

                else:
                    pass

        else:
            pass

    else:
        pass

