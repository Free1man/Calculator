# -*- coding: utf-8 -*-
def menu(x,y,z):
        print "1: BIN "
        print "2: HEX "

        while True:

            choice = int(raw_input("BIN или HEX "))

            if choice == 1:
                print x + 'Cложение BIN'
                print y()

            elif choice == 2:
                print x + 'Cложение HEX'
                print z()
            else:
                print "введите 1 или 2 "

def doBin(sign,result):

    shownResult = ""
    while result > 0:
        modulo = str(result % 2)
        shownResult = modulo + shownResult
        result = int(result / 2)
    if 8 >= len(shownResult) > 0:
        shownResult = 'b'+str(sign)+'0'*(8 - len(shownResult)-1)+str(shownResult)
    elif 16 >= len(shownResult) > 8:
        shownResult = 'b'+str(sign)+'0'*(16 - len(shownResult)-1)+str(shownResult)
    elif 32 >= len(shownResult) > 16:
        shownResult = 'b'+str(sign)+'0'*(32 - len(shownResult)-1)+str(shownResult)
    elif 64 >= len(shownResult) > 32:
        shownResult = 'b'+str(sign)+ '0'*(64 - len(shownResult)-1)+str(shownResult)
    return shownResult

def calculationBin(result):

    if result > 0:
        sign = 0
        return doBin(sign,result)

    elif result < 0:

        result = -result
        sign = 1
        return doBin(sign,result)

    elif result == 0:

        return 0

def calculationHex(result):
    shownResult = ""

    if result > 0:

        while result > 0:
            modulo = result % 16
            if modulo == 10:
                modulo = 'A'
            elif modulo == 11:
                modulo = 'B'
            elif modulo == 12:
                modulo = 'C'
            elif modulo == 13:
                modulo = 'D'
            elif modulo == 14:
                modulo = 'E'
            elif modulo == 15:
                modulo = 'F'
            elif modulo < 10:
                modulo = str(modulo)

            shownResult = modulo + shownResult
            result = int(result / 16)
        return (shownResult)

    elif result < 0:

        return "---"

def additionBin():
    print "Введите два чилса для сложения"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))
    result = int(firstNumber + secondNumber)
    print calculationBin(result)

def additionHex():
    print "Введите два чилса для сложения"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))
    result = int(firstNumber + secondNumber)
    print calculationHex(result)

def subtractionBin():
    return "Введите два чилса для вычитания"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))
    result = int(firstNumber - secondNumber)
    print calculationBin(result)

def subtractionHex():
    print "Введите два чилса для вычитания"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))
    result = int(firstNumber - secondNumber)
    print calculationHex(result)

__name__ == '__main__'

print "1: +"
print "2: -"
print "0: выход"

while True:

    choice = int(raw_input("Выберите действие из списка  "))

    if choice == 1:
        x = 'сложение'
        y = additionBin
        z = additionHex

        menu(x,y,z)

    elif choice == 2:
        x = 'сложение'
        y = additionBin
        z = additionHex

        menu(x,y,z)

    elif choice == 0:
        exit()
    else:
        print "введите 1 или 2 "

