str = input("File name: ")

extensions = []

images = ['jpg', 'jpeg', 'png', 'gif']
apps = ['pdf', 'txt', 'zip']
lower = str.lower()
lower = lower.replace(" ", "")

double = []

for i in range(len(lower)):
    if lower[i] == '.':
         double.append(lower[i+1::])

if double[-1] in images:
    print("image/"+double[-1])
elif double[-1] in apps:
    print("application/"+double[-1])
else:
    print("application/octet-stream")