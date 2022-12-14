kezd:int=None
veg:int=None
i:int=None
osszeg:int=0
szorzat:int=1


print("Adjon meg egy számot: ",end='')
kezd=int(input())
print("Adjon meg egy másik számot: ",end='')
veg=int(input())

for i in range(kezd, veg):
    osszeg+=i
    print(i)
print(osszeg)

for i in range(kezd, veg):
    szorzat*=i
    print(i)
print(szorzat)
