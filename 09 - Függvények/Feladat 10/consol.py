import random

def getNumber1()->int:
    number: int = None
    temp: str = None
    truncatedString:float=None
    while(number==None or (number < 0 or number > 9)):
        print("Adja meg az első számot 0-9 között: ",end="")
        temp = input()
        truncatedString = temp.replace("-","").replace(".","")
        if(temp.isnumeric):
            number=int(truncatedString)
        else:
            print("Nem számot adott meg!")
    return number



def getNumber2()->int:
    number: int = None
    temp: str = None
    truncatedString:float=None
    while(number==None or (number < 40 or number > 50)):
        print("Adja meg az első számot 40-50 között: ",end="")
        temp = input()
        truncatedString = temp.replace("-","").replace(".","")
        if(temp.isnumeric):
            number=int(truncatedString)
        else:
            print("Nem számot adott meg!")
    return number

def getRandom(number1:int, number2:int)->int:
    randomNumber=random.randint(number1, number2)
    return randomNumber


