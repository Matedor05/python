tempSmall:str=None
tempBig:str=None
numberSmall:int=None
numberBig:int=  None

while(numberSmall==None or numberBig==None or numberBig<=numberSmall):
    print("Adja meg az első számot")
    tempSmall = input()
    print("Adja meg a második számot")
    tempBig = input()
    if(tempSmall.isnumeric() and tempBig.isnumeric()):
        numberSmall=int(tempSmall)
        numberBig=int(tempBig)
print("Számok:")
for i in range(numberBig, numberSmall-1,-1):
    print(i)
