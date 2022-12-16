kezd:int=None
veg:int=None
i:int=None
het:int=0
ot:int=0

print("Adja meg a kezdőértéket: ",end='')
kezd=int(input())
print("Adja meg a végértéket: ",end='')
veg=int(input())

for i in range(kezd, veg+1, 1):
    if(i%5==0 and i%7==0):
        ot+=1
        het+=1
    elif(i%7==0):
        het+=1
    elif(i%5==0):
        ot+=1

print(ot)
print(het)
if(ot>het):
   print("az öttel osztható számok összege a nagyobb")
elif(het>ot):
   print("a héttel osztható számok összege a nagyobb")
else:
   print("egyenlő az összeg")