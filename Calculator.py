# -*- coding: utf-8 -*-
def menu(operationLabel,operationBin,operationHex):
        print "1: BIN "
        print "2: HEX "

        while True:

            choice = raw_input("BIN или HEX ")

            if choice == '1':
                print operationLabel + ' BIN'
                return operationBin()

            elif choice == '2':
                print operationLabel + ' HEX'
                return operationHex()
            else:
                print "введите 1 или 2 "

def doBin(sign,result,type):

    shownResult = ""
    while result > 0:
        modulo = str(result % 2)
        shownResult = modulo + shownResult
        result = int(result / 2)

    if 8 >= len(shownResult) > 0:
        shownResult = type+str(sign)+'0'*(8 - len(shownResult)-sign)+str(shownResult)
    elif 16 >= len(shownResult) > 8:
        shownResult = type+str(sign)+'0'*(16 - len(shownResult)-sign)+str(shownResult)
    elif 32 >= len(shownResult) > 16:
        shownResult = type+str(sign)+'0'*(32 - len(shownResult)-sign)+str(shownResult)
    elif 64 >= len(shownResult) > 32:
        shownResult = type+str(sign)+ '0'*(64 - len(shownResult)-sign)+str(shownResult)
    return shownResult

def calculationBin(result):

    if result > 0:
        sign = 0
        type='b'
        return doBin(sign,result,type)

    elif result < 0:

        result = -result
        sign = 1
        type='b'
        return doBin(sign,result,type)

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

    if result < 0:

        result = -result
        nextHex = 0
        while result > 0:
            modulo = result % 16
            modulo = 16 - modulo

            if nextHex == -1:
                modulo = modulo - 1

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
            if result > 16:
                nextHex = -1
            result = int(result / 16)


        if 8 >= len(shownResult) > 0:
            shownResult ='0x' + 'F'*(8 - len(shownResult))+str(shownResult)
        elif 16 >= len(shownResult) > 8:
            shownResult ='0x' + 'F'*(16 - len(shownResult))+str(shownResult)
        elif 32 >= len(shownResult) > 16:
            shownResult ='0x' + 'F'*(32 - len(shownResult))+str(shownResult)
        elif 64 >= len(shownResult) > 32:
            shownResult ='0x' + 'F'*(64 - len(shownResult))+str(shownResult)
        print shownResult

def additionBin():

    print "Введите два числа для сложения"
    try:
        firstNumber = int(raw_input("Первое число: "))
        secondNumber = int(raw_input("Второе число: "))
        result = int(firstNumber + secondNumber)
        print calculationBin(result)
    except ValueError:
        print "Неверный ввод, возможно вводить только цифры"


def additionHex():
    
    try:
        print "Введите два числа для сложения"
        firstNumber = int(raw_input("Первое число: "))
        secondNumber = int(raw_input("Второе число: "))
        result = int(firstNumber + secondNumber)
        print calculationHex(result)
    except ValueError:
        print "Неверный ввод, возможно вводить только цифры"

def subtractionBin():
    
    try:    
        print "Введите два числа для вычитания"
        firstNumber = int(raw_input("Первое число: "))
        secondNumber = int(raw_input("Второе число: "))
        result = int(firstNumber - secondNumber)
        print calculationBin(result)
    except ValueError:
        print "Неверный ввод, возможно вводить только цифры"
    

def subtractionHex():
    try:   
        print "Введите два с для вычитания"
        firstNumber = int(raw_input("Первое число: "))
        secondNumber = int(raw_input("Второе число: "))
        result = int(firstNumber - secondNumber)
        print calculationHex(result)
    except ValueError:
        print "Неверный ввод, возможно вводить только цифры"

__name__ == '__main__'

while True:

    print "1: +"
    print "2: -"
    print "0: выход"

    choice = raw_input("Выберите действие из списка  ")

    if choice == '1':
        operationLabel = 'Сложение'
        operationBin = additionBin
        operationHex = additionHex

        menu(operationLabel,operationBin,operationHex)

    elif choice == '2':
        operationLabel = 'Вычитание'
        operationBin = subtractionBin
        operationHex = subtractionHex

        menu(operationLabel,operationBin,operationHex)

    elif choice == 0:
        exit()
    else:
        print "введите 1 или 2 "

