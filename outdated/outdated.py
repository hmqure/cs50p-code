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

while True:
    try:
        broken = False
        item = input("Date:")
        rep = item.replace("/","_").replace(" ","_").replace(",","_")
        split = rep.split("_")

        for i in split:
            if i == "":
                split.remove(i)

        if 1 <= int(split[1]) <= 31:

            if split[0].isdigit() is False:
                for i in range(len(months)):
                    if months[i] == split[0]:
                        print((f"{int(split[2]):04}")+"-"+(f"{i+1:02d}")+"-"+(f"{int(split[1]):02d}"))
                        broken = True
                        break

            elif split[0].isdigit() is True:
                if 1 <= int(split[0]) <= 12:
                    print((f"{int(split[2]):04}")+"-"+(f"{int(split[0]):02d}")+"-"+(f"{int(split[1]):02d}"))
                    broken = True
                    break
                else:
                    pass

        else:
            pass

    except EOFError as e:
        pass
