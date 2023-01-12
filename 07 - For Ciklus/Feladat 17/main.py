startVal:int=None
endVal:int=None
sum:int=0

db:int=0

result:int=0


print("Adja meg a kezdőértéket")
kezd=int(input())
print("Adja meg a végértéket")
veg=int(input())

for i in range(kezd, veg+1, 1):
        sum+=i
        db+=1

result=sum/db

print("Átlag:")
print(result)
