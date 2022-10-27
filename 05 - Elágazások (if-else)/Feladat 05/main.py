num1:int=None
num2:int=None

print("Adjon meg 2 számot")
num1=int(input())
num2=int(input())

if(num1 < num2):
    print(f"{num1};{num2}")
elif(num1 > num2):
    print(f"{num2};{num1}")
else:
    print("a két szám egyenlő")