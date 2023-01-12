startVal:int=None
endVal:int=None
sum1:int=0
sum2:int=0
osszeg:int=0

print("Adja meg a kezdőértéket")
kezd=int(input())
print("Adja meg a végértéket")
veg=int(input())
if(kezd%2==0):
    kezd+=1
for i in range(kezd, veg+1, 1):
    if i%2!=0:
        sum1+=i
    elif i%2==0:
        sum2+=i

osszeg=sum1-sum2
print(osszeg)

