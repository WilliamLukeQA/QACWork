file = input("Please Enter File Name")
openfile = open(file, "r")
data = openfile.read()

f = open(file, "w")
for char in data:
    char = ord(char) + 10
    f.write(str(char))




