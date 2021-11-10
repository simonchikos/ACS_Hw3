# coding=utf-8
from number import *
# ----------------------------------------------


class Complex(Number):
    def __init__(self):
        self.real = 0.0
        self.imaginary = 0.0

    def ReadStrArray(self, str_array, i):
        # должно быть как минимум два непрочитанных значения в массиве
        if i >= len(str_array) - 1:
            return 0
        self.real = float(str_array[i])
        self.imaginary = float(str_array[i + 1])
        i += 2
        # print("Complex Number: real = ", self.real, " imaginary = ", self.imaginary)
        return i

    def Randomise(self):
        self.real = random.random() * 20 + 0.000001
        self.imaginary = random.random() * 20 + 0.000001

    def Print(self):
        print("It is Complex Number: real = ", self.real, " imaginary = ", self.imaginary, ", value = ", self.Cast())

    def Write(self, ostream):
        ostream.write(
            "It is Complex Number: real = {}  imaginary = {}, value = {}".format(self.real, self.imaginary, self.Cast()))

    def Cast(self):
        return (self.real * self.real + self.imaginary * self.imaginary) ** 0.5
