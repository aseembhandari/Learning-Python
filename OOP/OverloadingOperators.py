# This program demonstrates the concept of Operator Overloading
class Vecotr:
    def __init__(self,a,b):
        self.a =a
        self.b =b

    def __str__(self):
        return 'Vector (%d,%d)' % (self.a,self.b)

    def __add__(self, other):
        return Vecotr(self.a + other.a, self.b + other.b)

v1 = Vecotr(2,10)
v2 = Vecotr (5,-2)
print (v1 + v2)