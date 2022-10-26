num1:int=None
num2:int=None
num3:int=None
num4:int=None
eredmeny:float=None

print("Adja meg az első számot")
num1=int(input())


print("Adja meg a második számot")
num2=int(input())

print("Adja meg a harmadik számot")
num3=int(input())

print("Adja meg a negyedik számot")
num4=int(input())

eredmeny=(num1+num2)/(num3-num4)

print(f"Az eredmeny {eredmeny:1.2f}")