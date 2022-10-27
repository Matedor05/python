num1:int=None
num2:int=None
num3:int=None

print("Adjon meg 3 számot")
num1=int(input())
num2=int(input())
num3=int(input())

if(num1 < num2 and num1 < num3 and num2 < num3):
    print(f"{num1};{num2};{num3}")
elif(num1 < num2 and num1 < num3 and num2 > num3):
    print(f"{num1};{num3};{num2}")
elif(num2 < num1 and num2 < num3 and num1 > num3):
    print(f"{num2};{num3};{num1}")

elif(num2 < num1 and num2 < num3 and num1 < num3):
    print(f"{num2};{num1};{num3}")
elif(num3 < num1 and num3 < num2 and num1 < num2):
    print(f"{num3};{num1};{num2}")
elif(num3 < num1 and num3 < num2 and num1 > num2):
    print(f"{num3};{num2};{num1}")    
else:
    print("a számokból valamelyik egyenlő a másikkal")