num1:int=None
num2:int=None

print("Adjon meg kéz számot")
num1=int(input())
num2=int(input())

if(num1 % num2 == 0):
    print("az első számnak osztója a második szám")
else:
    print("A második szám nem oszója sz első számnak")