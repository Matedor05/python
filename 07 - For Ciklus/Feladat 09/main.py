kezd:int=None
veg:int=None
eredmeny:int=None

print("Adjon meg egy számot: ",end='')
kezd=int(input())
print("Adjon meg egy másik számot: ",end='')
veg=int(input())
eredmeny=kezd+veg
for eredmeny in range(kezd, veg, 2):
    if(kezd%2!=0):
        kezd+=1
        print(eredmeny)