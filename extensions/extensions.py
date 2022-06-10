str = input("File name: ")

extensions = []

images = ['jpg', 'jpeg', 'png', 'gif']
apps = ['pdf', 'txt', 'zip']
lower = str.lower()
lower = lower.replace(" ", "")

for i in range(len(lower)):
    if lower[i] == '.':
        ext = lower[i+1::]
        if ext in images:
            print("image/"+ext)
        elif ext in apps:
            print("application/"+ext)
        else:
            print("application/octet-stream")

if "." not in lower:
    print("application/octet-stream")