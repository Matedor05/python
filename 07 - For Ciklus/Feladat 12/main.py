kezd:int=None
veg:int=None
i1:int=None
i2:int=None
osszeg1:int=0
osszeg2:int=0

print("Adja meg a kezdőértéket: ",end='')
kezd=int(input())
print("Adja meg a végértéket: ",end='')
veg=int(input())

if(kezd%2!=0):
    kezd+=1
for i1 in range(kezd, veg, 2):
    osszeg1+=i1
    print(i1)
print(osszeg1)

if(kezd%2==0):
    kezd+=1
for i2 in range(kezd, veg, 2):
    osszeg2+=i2
    print(i2)
print(osszeg2)
if(osszeg1>osszeg2):
   print("a páros számok összege a nagyobb")