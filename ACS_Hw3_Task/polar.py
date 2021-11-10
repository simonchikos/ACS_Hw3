# coding=utf-8
from number import *
# ----------------------------------------------


class Polar(Number):
    def __init__(self):
        self.angle = 0.0
        self.radius = 0.0

    def ReadStrArray(self, str_array, i):
        # должно быть как минимум два непрочитанных значения в массиве
        if i >= len(str_array) - 1:
            return 0
        self.angle = float(str_array[i])
        self.radius = float(str_array[i + 1])
        i += 2
        # print("Polar: radius = ", self.radius, " angle = ", self.angle)
        return i

    def Randomise(self):
        self.angle = random.random() * 20 + 0.000001
        self.radius = random.random() * 20 + 0.000001

    def Print(self):
        print("It is Polar Coords: radius = ", self.radius, " angle = ", self.angle, ", value = ", self.Cast())

    def Write(self, ostream):
        ostream.write(
            "It is Polar Coords: radius = {}  angle = {}, value = {}".format(self.radius, self.angle, self.Cast()))

    def Cast(self):
        return self.radius
