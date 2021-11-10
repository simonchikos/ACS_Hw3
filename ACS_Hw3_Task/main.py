# coding=utf-8
import sys
import string
import os.path

from extender import *

#----------------------------------------------
if __name__ == '__main__':
    inputFileName, outputFileName, outputFileNameAfterSort = "./../ACS_Hw3_Tests/", "./../ACS_Hw3_Results/", "./../ACS_Hw3_Sorted_Results/"
    length = 0

    if len(sys.argv) != 5:
        print("incorrect command line!\n  Waited:\n     command -f infile outfile01 outfile02\n")
        print("  Or:\n     command -n number outfile01 outfile02\n")
        exit()
    else:
        print('==> Start')
        inputFileName += sys.argv[2]
        outputFileName += sys.argv[3]
        outputFileNameAfterSort += sys.argv[4]

    container = Container()
    if sys.argv[1] == "-f":
        if not os.path.isfile(inputFileName):
            print("incorrect Name Of File!\n")
            exit()
        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()
        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = str.replace("\n", " ").split(" ")
        length = ReadStrArray(container, strArray)
    else:
        if sys.argv[1] != "-n":
            print("incorrect qualifier value!\n  Waited:\n     command -f infile outfile01 outfile02\n")
            print("  Or:\n     command -n number outfile01 outfile02\n")
            exit()
        # Заполняем контейнер произвольными значениями
        length = int(sys.argv[2])
        Randomise(container, length)
    # Выводим размер контейнера.
    print("size = \n", length)
    # Выводим содержимое контейнера.
    container.Print()
    # Выводим содержимое контейнера в файл.
    ofile = open(outputFileName, 'w')
    container.Write(ofile)
    ofile.close()
    # Сортируем контейнер, и повтороно выводим содержимое контейнера в файл.
    ofile = open(outputFileNameAfterSort, 'w')
    container.BinaryInsertion()
    container.Print()
    container.Write(ofile)
    ofile.close()

    print('==> Finish')
