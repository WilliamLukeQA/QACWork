class one:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c

    def __add__(self, q):
        luke = one(0,0,0)
        luke.x = self.x + q.x
        luke.y = self.y + q.y
        luke.z = self.z + q.z
        return luke

    def __str__(self):
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z)

A = one(10, 20, 30)
B = one(1, 2, 3)
X = A + B
print(X)
