def encrypt(x):
    blah = ""
    for char in x:
        blah = blah + chr(ord(char) + 1)
    print(blah)
    return blah

def decrypt(x):
    blah = ""
    for char in x:
        blah = blah + chr(ord(char) - 1)
    print(blah)
    return blah


loop = 1

while loop == 1:
    print("1 Encrypt\n 2 Decrypt\n 3 Quit")
    selection = input("Enter an option number")
    if int(selection) == 1:
        inputfile = input("Encrypt input filename?")
        outputfile = input("Encrypt output filename")
        inputfileobj = open(inputfile, "r")
        data = inputfileobj.read()
        print(data)
        outputfileobj = open(outputfile, "a")
        outputfileobj.write(encrypt(data))
        inputfileobj.close()
        outputfileobj.close()
    if int(selection) == 2:
        inputfile = input("Encrypt input filename?")
        outputfile = input("Encrypt output filename")
        inputfileobj = open(inputfile, "r")
        data = inputfileobj.read()
        print(data)
        outputfileobj = open(outputfile, "a")
        outputfileobj.write(decrypt(data))
        inputfileobj.close()
        outputfileobj.close()
