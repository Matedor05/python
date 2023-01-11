kezd:int=None
veg:int=None
i:int=None
osszeg:int=0

print("Adja meg a kezdőértéket: ",end='')
kezd=int(input())
print("Adja meg a végértéket: ",end='')
veg=int(input())

if(kezd%2!=0):
    kezd+=1
for i in range(kezd, veg+1, 2):
    osszeg+=i
    print(i)
print(osszeg)