/number: float = None
temp: str = None
isNumber: bool = False
truncatedString:float=None


while(number==None or (number < 0 or number > 9)):
    print("Adjon meg egy számot:",end="")
    temp = input()
    truncatedString = temp.replace("-","").replace(".","")
    if(temp.isnumeric):
        isNumber = temp()

    if(isNumber):
        number = float(temp)
    else:
        print("Nem számot adott meg!")