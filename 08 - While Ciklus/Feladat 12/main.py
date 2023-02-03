solution:int=None
month:int=0
number:int=None
osszeg:int=None


print("Adja meg mennyi pénzt rak be a bankba")
number=int(input())
osszeg=int(number)
while(osszeg<100000):
    month+=1
    osszeg=osszeg*1.02
print(month)
print(osszeg)


