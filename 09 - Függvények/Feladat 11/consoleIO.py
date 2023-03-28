def getName()->str:
        name : str = None
        inputName : str = None
        while(name==None):
                print("Kérem adja meg a nevét!")
                inputName = input()
                name=str(inputName)
        return name.strip().capitalize()

def getHours()->int:
    hour: int = None
    temp: str = None
    truncatedString:float=None
    while(hour==None or (hour < 39)):
        print("Adja meg a ledolgozott órák számát!")
        temp = input()
        truncatedString = temp.replace("-","").replace(".","")
        if(temp.isnumeric):
            hour=int(truncatedString)
        else:
            print("Nem számot adott meg!")
    return hour