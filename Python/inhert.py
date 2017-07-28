class Parent(object):
    def __init__(self):
        print("Hello")


class Child1(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Hey")


class Child2(Parent):
    def __init__(self):
        print("Bye")

Child1();