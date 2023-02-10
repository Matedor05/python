from random import randint
from sysconfig import parse_config_h
temp1:str=None
temp2:str=None
number1:int=None
number2:int=None
random:int=None
atlag=float=0
db:int=0
db2:int=0
while(number1==None or number2==None or number1>number2 or number1%2!=0 or number2%2==0):
    print("Adjon meg egy páros számot")
    temp1=input()
    if(temp1.isnumeric):
        number1=int(temp1)
    print("Adjon meg egy páratlan számot")
    temp2=input()
    if(temp2.isnumeric):
        number2=int(temp2)

random=randint(number1,number2)
for i in range(number1,number2+1,1):
    if(i%4==0):
        db+=1
    atlag+=i
    db2+=1
atlag=atlag/db2

if(atlag>random):
    print("A páratlan számtól van messzebb a random szám")
elif(atlag<random):
    print("A páros számtól van messzebb a random szám")
print(f"Átlag: {atlag}")
print(f"4-gyel osztható számok darabszáma:{db}")



