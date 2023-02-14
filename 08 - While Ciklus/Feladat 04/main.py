from base64 import encode
from random import randint

temp:str=None
number:int=None
osszeg:int=0
db:int=0
while(osszeg<100):
    print("Adjon meg egy számot")
    temp=input()
    if (temp.isnumeric()):
        number=int(temp)
    else:
        continue
    osszeg+=number
    db+=1
    print(f"A számok összege: {osszeg}")
    print(f"Próbálkozások száma: {db}")
if(osszeg>=100):
    print("A számok összege elérte a 100-at ezért vége")
    