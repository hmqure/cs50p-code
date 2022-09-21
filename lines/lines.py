import sys

sys = sys.argv

print(sys)

if len(sys) > 2:
    print("Too many command-line arguments")

elif len(sys) == 1:
    print("Too few command-line arguments")

elif len(sys) == 2:
    if