kezd:int=None
veg:int=None
i:int=None
eredmeny:int=0

print("Adja meg a kezdőértéket: ",end='')
kezd=int(input())
print("Adja meg a végértéket: ",end='')
veg=int(input())

for i in range(kezd, veg):
    if(i%3==0):
        eredmeny+=1
print(eredmeny)