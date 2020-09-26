import string
import random

lastpass = []

def checkSymbol():
    arrSym = []
    arrUpper = input("Вам нужны символы верхнего регистра?(y/n)\n")
    if arrUpper == "y":
        arrSym.extend(string.ascii_uppercase)
    arrLower = input("Вам нужны символы нижнего регистра?(y/n)?\n")
    if arrLower == "y":
        arrSym.extend(string.ascii_lowercase)
    arrDig = input("Вам нужны целые числа?(y/n)\n")
    if arrDig == "y":
        arrSym.extend(string.digits)
    arrPunc = input("Вам нужны знаки препинания?(y/n)\n")
    if arrPunc == "y":
        arrSym.extend(string.punctuation)
    random.shuffle(arrSym)
    return arrSym

def lenPass():
    try:
        lenPassword = int(input("Введите длинну пароля:"))
        return lenPassword
    except ValueError:
        print("\n Принимаются только числовые значения!")

def genPass():
    chSym = checkSymbol()
    lastpass = ''
    for i in range(lenPass()):
        lastpass += random.choice(chSym)
    return print(f"Ваш сгенерированный пароль: {lastpass}")
genPass()