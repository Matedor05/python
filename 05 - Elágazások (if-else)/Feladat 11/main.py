num1:int=None

print("Adjon meg egy számot")
num1=int(input())

if(num1 % 2 == 0):
    print("A szám páros")
else:
    print("A szám páratlan")

if(num1>=1):
    print("A szám pozitív")
elif(num1<=-1):
    print("A szám negatív")
elif(num1==0):
    print("A szám a 0")

if(num1 %5 ==0):
    print("a szam osztható 5-tel")
else:
    print("a szam nem osztható 5-tel")