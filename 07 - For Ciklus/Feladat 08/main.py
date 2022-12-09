kezd:int=None
veg:int=None
eredmeny:int=None

print("Adja meg a kezdőértéket: ",end='')
kezd=int(input())
print("Adja meg a végértéket: ",end='')

veg=int(input())
eredmeny=kezd+veg
for eredmeny in range(kezd, veg, 1):
    if(kezd%2==0):
        kezd+=1
        print(eredmeny)
    