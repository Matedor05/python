kezd:int=None
veg:int=None
i:int=None
eredmeny:int=0

print("Adja meg a kezdőértéket")
kezd=int(input())
print("Adja meg a végértéket")
veg=int(input())
for i in range(kezd, veg+1, 1):
    if(i%3==0 and i%2!=0):
        eredmeny+=1
print(eredmeny)
