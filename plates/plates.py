def main():
    plate = input("Plate: ")
    if is_valid(plate) is True:
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    zero = []
    num = ''
    if 2 <= len(s) <= 6 and s.isalpha() is not True:
        if s[0:2].isalpha() is True:
            if s.isalnum() is True:
                for i in range(len(s)):
                    if s[i].isdigit() is True:
                        zero.append(s[i])
                        if s[i].isdigit() is True:
                            num += s[i::]
                            if num.isdigit() is True:
                                if zero[0] != '0' and s[-1].isnumeric() is True:
                                    return True

    elif 2 <= len(s) <= 6 and s.isalpha() is True:
        return True

main()