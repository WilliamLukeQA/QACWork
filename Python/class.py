class ONS:
    def message(self):
        print("Hello")
        self.add(7,2)

    def add(self,b,c):
        c = b + c
        print("Result: %d" % c)

ref = ONS()
ref.message()
