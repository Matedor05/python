from base64 import encode
from random import randint

temp: str = None
number: int = None
while(number==None):
    print("Adj meg az életkorát!")
    temp = input()
    if (temp.isnumeric()):
        number=int(temp)
if(number>0 and number<=6):
    print("Gyerek korosztályba tartozik")
elif(number>6 and number<=18):
    print("Iskolás korosztályba tartozik")
elif(number>18 and number<=65):
    print("Dolgozó korosztályba tartozik")
elif(number>65 and number<=132):
    print("Nyugdíjas korosztályba tartozik")
else:
    print("Maga egy ufó")

