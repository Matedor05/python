startVal:int=None
endVal:int=None
sum1:int=0
sum2:int=0
db1:int=0
db2:int=0
result1:int=0
result2:int=0

print("Adja meg a kezdőértéket")
kezd=int(input())
print("Adja meg a végértéket")
veg=int(input())

for i in range(kezd, veg+1, 1):
    if(i%2==0):
        sum1+=i
        db1+=1
    elif(i%2!=0):
        sum2+=i
        db2+=1


result1=sum1/db1
result2=sum2/db2

print("Paros:")
print(result1)
print("Paratlan:")
print(result2)