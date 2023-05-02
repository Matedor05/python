import random

def getNumber(kezdo:int, vegertek:int)->int:
    number: int = None
    temp: str = None
    truncatedString:float=None
    while(number==None or (number < kezdo or number > vegertek)):
        print(f"Adja meg az első számot {kezdo} és {vegertek} között: ",end="")
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


