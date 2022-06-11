def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        return



def convert(time):
    split = time.split(":")
    hour = int(split[0])
    minute = ((int(split[1]))/6)/10
    return hour+minute


if __name__ == "__main__":
    main()