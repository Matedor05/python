from base64 import encode
from random import randint

solution:int=None
tries:int=0
number:int=None
temp:str=None

solution=randint(1,9)

while(tries<5 and solution!=number):
    print("Találja ki a számot:",end="")
    temp = input()
    if(temp.isnumeric):
        number = temp()

    if(solution == number):
        print("Ön nyert")
    else:
        tries+=1
if(tries==5):
    print("Nem nyert")
        