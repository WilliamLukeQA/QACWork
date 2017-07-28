loop = 1


while loop == 1:
    print("1 = Additiion")
    print("2 = Substraction")
    print("3 = Division")
    print("4 = Multiply")
    print("5 = Timestable")

    choice = input("Please Enter Your Choice")

    def numberone():
        return input("Enter First Number:")

    def numbertwo():
        return input("Enter Second Number:")


    def add(a, b):
        return a + b


    def subtract(a, b):
        return a - b


    def division(a, b):
        return a / b


    def multiplication(a, b):
        return a * b


    def table(a):
        for i in range(1, 11):
            print(a, 'x', i, '=', a * i)

    if int(choice) == 1:
        loopadd = 1
        while loopadd == 1:
            print(add(int(numberone()), int(numbertwo())))
            repeat = input("Repeat?")
            if repeat == "n":
                loopadd = 0

    if int(choice) == 2:
        loopsub = 1
        while loopsub == 1:
            print(subtract(int(numberone()), int(numbertwo())))
            repeat = input("Repeat?")
            if repeat == "n":
                loopsub = 0

    if int(choice) == 3:
        loopdiv = 1
        while loopdiv == 1:
            print(division(int(numberone()), int(numbertwo())))
            repeat = input("Repeat?")
            if repeat == "n":
                loopdiv = 0

    if int(choice) == 4:
        loopmulti = 1
        while loopmulti == 1:
            print(multiplication(int(numberone()), int(numbertwo())))
            repeat = input("Repeat?")
            if repeat == "n":
                loopmulti = 0

    if int(choice) == 5:
        looptable = 1
        while looptable == 1:
            a = input("NJN")
            print(table(a))
            repeat = input("Repeat?")
            if repeat == "n":
                looptable = 0







