# -*- coding: utf-8 -*-
def additionBin():
    print "Введите два чилса для сложения"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber + secondNumber)
    shownResult = ""
    if result > 0:
        while result > 0:
            modulo = str(result % 2)
            shownResult = modulo + shownResult
            result = int(result / 2)

        if 8 > len(shownResult) > 0:
            shownResult = 'b'+'0'*(8 - len(shownResult))+str(shownResult)
        elif 16 > len(shownResult) > 8:
            shownResult = 'b'+'0'*(16 - len(shownResult))+str(shownResult)
        elif 32 > len(shownResult) > 16:
            shownResult = 'b'+'0'*(32 - len(shownResult))+str(shownResult)
        elif 64 > len(shownResult) > 32:
            shownResult = 'b'+'0'*(64 - len(shownResult))+str(shownResult)


    elif result < 0:
        result = -result
        while result > 0:
            modulo = str(result % 2)
            shownResult = modulo + shownResult
            result = int(result / 2)
        if 8 > len(shownResult) > 0:
            shownResult = 'b1'+'0'*(8 - len(shownResult)-1)+str(shownResult)
        elif 16 > len(shownResult) > 8:
            shownResult = 'b1'+'0'*(16 - len(shownResult)-1)+str(shownResult)
        elif 32 > len(shownResult) > 16:
            shownResult = 'b1'+'0'*(32 - len(shownResult)-1)+str(shownResult)
        elif 64 > len(shownResult) > 32:
            shownResult = 'b1'+'0'*(64 - len(shownResult)-1)+str(shownResult)

    elif result == 0:

        print 0

    return shownResult




def additionHex():
    print "Введите два чилса для сложения"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber + secondNumber)
    shownResult = ""

    while result > 0:
        modulo = result % 16
        if modulo == 10:
            modulo = 'A'
        if modulo == 11:
            modulo = 'B'
        if modulo == 12:
            modulo = 'C'
        if modulo == 13:
            modulo = 'D'
        if modulo == 14:
            modulo = 'E'
        if modulo == 15:
            modulo = 'F'
        if modulo < 10:
            modulo = str(modulo)

        shownResult = modulo + shownResult
        result = int(result / 16)

    return (shownResult)


def subtractionBin():
    print "Введите два чилса для вычитания"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber - secondNumber)
    shownResult = ""

    if result > 0:
        while result > 0:
            modulo = str(result % 2)
            shownResult = modulo + shownResult
            result = int(result / 2)
        if 8 > len(shownResult) > 0:
            shownResult = 'b'+'0'*(8 - len(shownResult))+str(shownResult)
        elif 16 > len(shownResult) > 8:
            shownResult = 'b'+'0'*(16 - len(shownResult))+str(shownResult)
        elif 32 > len(shownResult) > 16:
            shownResult = 'b'+'0'*(32 - len(shownResult))+str(shownResult)
        elif 64 > len(shownResult) > 32:
            shownResult = 'b'+'0'*(64 - len(shownResult))+str(shownResult)


    elif result < 0:
        result = -result
        while result > 0:
            modulo = str(result % 2)
            shownResult = modulo + shownResult
            result = int(result / 2)
        if 8 > len(shownResult) > 0:
            shownResult = 'b1'+'0'*(8 - len(shownResult)-1)+str(shownResult)
        elif 16 > len(shownResult) > 8:
            shownResult = 'b1'+'0'*(16 - len(shownResult)-1)+str(shownResult)
        elif 32 > len(shownResult) > 16:
            shownResult = 'b1'+'0'*(32 - len(shownResult)-1)+str(shownResult)
        elif 64 > len(shownResult) > 32:
            shownResult = 'b1'+'0'*(64 - len(shownResult)-1)+str(shownResult)

    return shownResult

def subtractionHex():
    print "Введите два чилса для вычитания"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber - secondNumber)
    shownResult = ""

    if result > 0:

        while result > 0:
            modulo = result % 16
            if modulo == 10:
                modulo = 'A'
            if modulo == 11:
                modulo = 'B'
            if modulo == 12:
                modulo = 'C'
            if modulo == 13:
                modulo = 'D'
            if modulo == 14:
                modulo = 'E'
            if modulo == 15:
                modulo = 'F'
            if modulo < 10:
                modulo = str(modulo)

            shownResult = modulo + shownResult
            result = int(result / 16)
        print (shownResult)

    elif result < 0:

        print "---"



print "1: +"
print "2: -"
print "0: выход"

while True:

    choice = int(raw_input("Выберите действие из списка  "))

    if choice == 1:
        print "1: BIN "
        print "2: HEX "

        while True:

            choice = int(raw_input("BIN или HEX "))

            if choice == 1:
                print 'Cложение BIN'
                print additionBin()

            elif choice == 2:
                print 'Cложение HEX'
                print additionHex()
            else:
                print "введите 1 или 2 "

    elif choice == 2:
        print "1: BIN "
        print "2: HEX "

        while True:

            choice = int(raw_input("BIN или HEX "))

            if choice == 1:
                print 'Вычитание BIN'
                print subtractionBin()


            elif choice == 2:
                print 'Вычитание HEX'
                print subtractionHex()
            else:
                print "введите 1 или 2 "

    elif choice == 0:
        exit()
    else:
        print "введите 1 или 2 "

