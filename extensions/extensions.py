str = input("File name: ")

extensions = []

images = ['jpeg', 'png', 'gif']
images2 = ['jpg']
text = ['txt']
apps = ['pdf', 'zip']
lower = str.lower()
lower = lower.replace(" ", "")

double = []
front = []

for i in range(len(lower)):
    if lower[i] == '.':
        double.append(lower[i+1::])
        front.append(lower[0:i])


if double[-1] in images:
    print("image/"+double[-1])
elif double[-1] in images2:
    print("image/jpeg")
elif double[-1] in text:
    print("text/"+front[0])
elif double[-1] in apps:
    print("application/"+double[-1])
else:
    print("application/octet-stream")

