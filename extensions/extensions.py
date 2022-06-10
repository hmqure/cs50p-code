str = input("File name: ")

extensions = []

images = ['jpg', 'jpeg', 'png', 'gif']
apps = ['pdf', 'txt', 'zip']
lower = str.lower()
lower = lower.replace(" ", "")

double = []

for i in range(len(lower)):
    count = lower.count(".")
    if count == 1:
        if lower[i] == '.':
            ext = lower[i+1::]
            if ext in images:
                print("image/"+ext)
            elif ext in apps:
                print("application/"+ext)
            else:
                print("application/octet-stream")
    if count != 1:
        if lower[i] == '.':
            double.append(lower[i+1::])


if double is not False:
    if double[-1] in images:
        print("image/"+double[-1])
    elif double[-1] in apps:
        print("application/"+double[-1])
    else:
        print("application/octet-stream")
else:
    pass




if "." not in lower:
    print("application/octet-stream")
         