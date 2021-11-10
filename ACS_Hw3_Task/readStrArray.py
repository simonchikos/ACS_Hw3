# coding=utf-8
from extender import *
import random


# Метод, читающий объекты из массива
def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)  # преобразование в целое
        # print("key = ", key)
        if key == 1:  # признак Дроби
            shape = Fraction()
        elif key == 2:  # признак Полярного Числа
            shape = Polar()
        elif key == 3:  # признак Комплексного числа
            shape = Complex()
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return figNum
        shape.ReadStrArray(strArray, i)  # чтение числа с возвратом позиции за ним
        i += 3
        figNum += 1
        container.store.append(shape)
    return figNum


# Метод, генерирующий size объектов
def Randomise(container, size):
    i = 0  # Индекс, задающий текущую строку в массиве
    while i < size:
        number_type = random.randint(0, 2)
        # print("key = ", key)
        if number_type == 0:  # признак дроби
            shape = Fraction()
        elif number_type == 1:  # признак полярного числа
            shape = Polar()
        else:  # признак комплексного числа
            shape = Complex()
        i += 1
        shape.Randomise()
        container.store.append(shape)
