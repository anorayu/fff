from math import pi
class Front:

    @staticmethod
    def rectactle(d,h):
        a = pi * d ** 2/4
        b = pi * d * h
        return round(a*2 +  b,  2)


    def __init__(self, di, hi):
        self.dia = di
        self.h = hi
        self.area = self.rectactle(di,hi)

a = Front(1,2)
print(a.rectactle(2,2))
print(a.area)
