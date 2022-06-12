months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

counter = 0

while counter == 0:
    try:
        item = input("Date:")
        rep = item.replace("/","_").replace(" ","_").replace(",","_")
        split = rep.split("_")

        for i in split:
            if i == "":
                split.remove(i)
        if split[1].isdigit() is True and split[2].isdigit() is True:
            if 1 <= int(split[1]) <= 31:

                if split[0].isdigit() is False:
                    for i in range(len(months)):
                        if months[i] == split[0]:
                            print((f"{int(split[2]):04}")+"-"+(f"{i+1:02d}")+"-"+(f"{int(split[1]):02d}"))
                            counter = counter + 1
                            break

                elif split[0].isdigit() is True:
                    if 1 <= int(split[0]) <= 12:
                        print((f"{int(split[2]):04}")+"-"+(f"{int(split[0]):02d}")+"-"+(f"{int(split[1]):02d}"))
                        counter = counter + 1
                        break
                    else:
                        pass

            else:
                pass

        else:
            pass

    except EOFError as e:
        pass