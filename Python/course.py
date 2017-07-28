class results:
    def __init__(self, x = 0, y = 0, z = 0):
            self.__phy = x
            self.__che = y
            self.__mat = z
            self.failed_course = 0

    def physics(self, p):
        if (p >= 0 and p <= 150):
            self.__phy = p
        else:
            print("Invalid score for Physics, score must be between 0 and 150")

    def chemistry(self, p):
        if (p >= 0 and p <= 150):
            self.__che = p
        else:
            print("Invalid score for Chemistry, score must be between 0 and 150")

    def maths(self, p):
        if (p >= 0 and p <= 150):
            self.__mat = p
        else:
            print("Invalid score for Maths, score must be between 0 and 150")

    def calculations(self):
        self.total = self.__phy + self.__mat + self.__che

    def showResults(self):
        self.calculations()
        print("Total score: ", + self.total)
        self.per = self.total * 100 / 450
        print("Percentage:", + self.per)

    def fail(self):
        self.failed_course = 0
        c = self.__che
        p = self.__phy
        m = self.__mat

        if c < 60:
            self.failed_course = self.failed_course + 1

        if p < 60:
            self.failed_course = self.failed_course + 1

        if m < 60:
            self.failed_course = self.failed_course + 1

        if self.failed_course == 1:
            print("You need to retake an exam")
        if self.failed_course == 2:
            print("You need to retake the course")
        if self.failed_course == 3:
            print("Go home")

Luke = results()
Luke.chemistry(150)
Luke.maths(150)
Luke.physics(100)
Luke.showResults()
Luke.fail()


