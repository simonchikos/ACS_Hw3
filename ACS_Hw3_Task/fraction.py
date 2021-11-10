# coding=utf-8
from number import *
# ----------------------------------------------


class Fraction(Number):
    def __init__(self):
        self.numerator = 0
        self.denominator = 0

    def ReadStrArray(self, str_array, i):
        # должно быть как минимум два непрочитанных значения в массиве
        if i >= len(str_array) - 1:
            return 0
        self.numerator = int(str_array[i])
        self.denominator = int(str_array[i + 1])
        i += 2
        # print("Fraction: numerator = ", self.numerator, " denominator = ", self.denominator)
        return i


    def Randomise(self):
        self.numerator = random.randint(1, 20)
        self.denominator = random.randint(1, 20)

    def Print(self):
        print("It is Fraction: numerator = ", self.numerator, " denominator = ", self.denominator, ", value = ", self.Cast())

    def Write(self, ostream):
        ostream.write(
            "It is Fraction: numerator = {}  denominator = {}, value = {}".format(self.numerator, self.denominator, self.Cast()))

    def Cast(self):
        return float(self.numerator) / float(self.denominator)
