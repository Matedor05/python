temp:str=None
number:int=None
while(number==None or number<99 or number>1000):
    print("Adjon meg egy háromjegyű, 7-tel osztható számot!")
    temp = input()
    if(temp.isnumeric()):
        number=int(temp)
if(number%7==0):
    print("Osztható 7-tel") 
else:
    print("Próbáld újra") 

