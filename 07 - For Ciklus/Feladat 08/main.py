kezd:int=None
veg:int=None
eredmeny:int=None

print("Adja meg a kezdőértéket: ",end='')
kezd=int(input())
print("Adja meg a végértéket: ",end='')

veg=int(input())
if(kezd%2!=0):
    kezd+=1
for eredmeny in range(kezd, veg, 2):
        print(eredmeny)
