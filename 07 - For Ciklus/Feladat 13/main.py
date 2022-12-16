kezd:int=None
veg:int=None
i:int=None
paros:int=0
paratlan:int=0

print("Adja meg a kezdőértéket: ",end='')
kezd=int(input())
print("Adja meg a végértéket: ",end='')
veg=int(input())

for i in range(kezd, veg+1, 1):
    if(i%2==0):
        paros+=1
    elif(i%2!=0):
        paratlan+=1


if(paros>paratlan):
   print("a páros számok összege a nagyobb")
else:
   print("a páratlan számok összege a nagyobb")
