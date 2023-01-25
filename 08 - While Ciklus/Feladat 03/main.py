from random import randint

solution:int=None
tries:int=0
number:int=None
temp:str=None

solution=randint(0,9)
while(tries<=5):
    print("Találja ki a számot:",end="")
    temp = input()
    if(temp.isnumeric()):
        number==int(temp)
    else:
        continue
    
    if(solution==temp):
        print("Ön nyert")
    else:
        number==None
if(tries==5):
    print("Nem nyert")
        