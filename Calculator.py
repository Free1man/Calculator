# -*- coding: utf-8 -*-
def additionBin():
    print "Введите два чилса для сложения"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber - secondNumber)
    n = ""
    if result > 0:
        while result > 0:
            y = str(result % 2)
            n = y + n
            result = int(result / 2)
        return n

    elif result < 0:
        z = -result
        while z > 0:
            y = str(z % 2)
            n = y + n
            z = int(z / 2)
    if 8 > len(n) > 0:
        n2 = 'b1'+'0'*(8 - len(n)-1)+str(n)
    elif 16 > len(n) > 8:
        n2 = 'b1'+'0'*(16 - len(n)-1)+str(n)
    elif 32 > len(n) > 16:
        n2 = 'b1'+'0'*(32 - len(n)-1)+str(n)
    elif 64 > len(n) > 32:
        n2 = 'b1'+'0'*(64 - len(n)-1)+str(n)

    return n2




def additionHex():
    print "Введите два чилса для сложения"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber + secondNumber)
    n = ""

    while result > 0:
        y = result % 16
        if y == 10:
            y = 'A'
        if y == 11:
            y = 'B'
        if y == 12:
            y = 'C'
        if y == 13:
            y = 'D'
        if y == 14:
            y = 'E'
        if y == 15:
            y = 'F'
        if y < 10:
            y = str(y)

        n = y + n
        result = int(result / 16)

    return (n)


def subtractionBin():
    print "Введите два чилса для вычитания"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber - secondNumber)
    n = ""

    if result > 0:
        while result > 0:
            y = str(result % 2)
            n = y + n
            result = int(result / 2)
        return n

    elif result < 0:
        z = -result
        while z > 0:
            y = str(z % 2)
            n = y + n
            z = int(z / 2)
    if 8 > len(n) > 0:
        n2 = 'b1'+'0'*(8 - len(n)-1)+str(n)
    elif 16 > len(n) > 8:
        n2 = 'b1'+'0'*(16 - len(n)-1)+str(n)
    elif 32 > len(n) > 16:
        n2 = 'b1'+'0'*(32 - len(n)-1)+str(n)
    elif 64 > len(n) > 32:
        n2 = 'b1'+'0'*(64 - len(n)-1)+str(n)

    return n2

def subtractionHex():
    print "Введите два чилса для вычитания"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber - secondNumber)
    n = ""

    if result > 0:
        result = int(firstNumber + secondNumber)
        n = ""

        while result > 0:
            y = result % 16
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            if y < 10:
                y = str(y)

            n = y + n
            result = int(result / 16)
        print (n)

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

# -*- coding: utf-8 -*-
def additionBin():
    print "Введите два чилса для сложения"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber + secondNumber)
    n = ""
    if result > 0:
        while result > 0:
            y = str(result % 2)
            n = y + n
            result = int(result / 2)

        if 8 > len(n) > 0:
            n2 = 'b'+'0'*(8 - len(n))+str(n)
        elif 16 > len(n) > 8:
            n2 = 'b'+'0'*(16 - len(n))+str(n)
        elif 32 > len(n) > 16:
            n2 = 'b'+'0'*(32 - len(n))+str(n)
        elif 64 > len(n) > 32:
            n2 = 'b'+'0'*(64 - len(n))+str(n)

    elif result < 0:
        z = -result
        while z > 0:
            y = str(z % 2)
            n = y + n
            z = int(z / 2)

        if 8 > len(n) > 0:
            n2 = 'b1'+'0'*(8 - len(n)-1)+str(n)
        elif 16 > len(n) > 8:
            n2 = 'b1'+'0'*(16 - len(n)-1)+str(n)
        elif 32 > len(n) > 16:
            n2 = 'b1'+'0'*(32 - len(n)-1)+str(n)
        elif 64 > len(n) > 32:
            n2 = 'b1'+'0'*(64 - len(n)-1)+str(n)

    return n2




def additionHex():
    print "Введите два чилса для сложения"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber + secondNumber)
    n = ""

    while result > 0:
        y = result % 16
        if y == 10:
            y = 'A'
        if y == 11:
            y = 'B'
        if y == 12:
            y = 'C'
        if y == 13:
            y = 'D'
        if y == 14:
            y = 'E'
        if y == 15:
            y = 'F'
        if y < 10:
            y = str(y)

        n = y + n
        result = int(result / 16)

    return (n)


def subtractionBin():
    print "Введите два чилса для вычитания"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber - secondNumber)
    n = ""

    if result > 0:
        while result > 0:
            y = str(result % 2)
            n = y + n
            result = int(result / 2)

        if 8 > len(n) > 0:
            n2 = 'b'+'0'*(8 - len(n))+str(n)
        elif 16 > len(n) > 8:
            n2 = 'b'+'0'*(16 - len(n))+str(n)
        elif 32 > len(n) > 16:
            n2 = 'b'+'0'*(32 - len(n))+str(n)
        elif 64 > len(n) > 32:
            n2 = 'b'+'0'*(64 - len(n))+str(n)

    elif result < 0:
        z = -result
        while z > 0:
            y = str(z % 2)
            n = y + n
            z = int(z / 2)

        if 8 > len(n) > 0:
            n2 = 'b1'+'0'*(8 - len(n)-1)+str(n)
        elif 16 > len(n) > 8:
            n2 = 'b1'+'0'*(16 - len(n)-1)+str(n)
        elif 32 > len(n) > 16:
            n2 = 'b1'+'0'*(32 - len(n)-1)+str(n)
        elif 64 > len(n) > 32:
            n2 = 'b1'+'0'*(64 - len(n)-1)+str(n)

    return n2

def subtractionHex():
    print "Введите два чилса для вычитания"
    firstNumber = int(raw_input("Первое число: "))
    secondNumber = int(raw_input("Второе число: "))

    result = int(firstNumber - secondNumber)
    n = ""

    if result > 0:
        result = int(firstNumber + secondNumber)
        n = ""

        while result > 0:
            y = result % 16
            if y == 10:
                y = 'A'
            if y == 11:
                y = 'B'
            if y == 12:
                y = 'C'
            if y == 13:
                y = 'D'
            if y == 14:
                y = 'E'
            if y == 15:
                y = 'F'
            if y < 10:
                y = str(y)

            n = y + n
            result = int(result / 16)
        print (n)

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

