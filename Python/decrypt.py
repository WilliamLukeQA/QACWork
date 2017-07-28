loop = 1


while loop == 1:
    choice = input("Please enter Decrypt or Encrypt")

    def en():
        def encrpyt():
            file = input("Please Enter File Name")
            openfile = open(file, "r")
            data = openfile.read()

            f = open(file, "w")
            for char in data:
                char = ord(char) + 10
                f.write(str(char))
                f.close()

    def decrpyt():
        defile = input("Please Enter File Name")
        opendefile = open(defile, "r")
        data = opendefile.read()

        f = open(defile, "w")
        for char in data:
            char = ord(char) - 10
            f.write(str(char))
            f.close()

    if str(choice) == "Encrypt":
        en()
        loop = 0

    if str(choice) == "Decrypt":
        decrpyt()
        loop = 0
