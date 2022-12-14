kezd:int=None
veg:int=None
eredmeny:int=None

print("Adjon meg egy számot: ",end='')
kezd=int(input())
print("Adjon meg egy másik számot: ",end='')
veg=int(input())
if(kezd%2!=0):
    kezd-=1
for eredmeny in range(kezd, veg, -2):
    print(eredmeny)