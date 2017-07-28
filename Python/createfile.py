msg = input("Want do you want write?")

F = open("Test.txt", "w")
F.write("Hello from the otherside!!! \n")
F.write(msg)
F.close()
