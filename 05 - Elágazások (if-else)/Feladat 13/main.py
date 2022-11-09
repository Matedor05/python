num:int=None

print("Adjon meg egy számot")
num=int(input())

if(0<=num and num<10):
    print("egyjegyű szám")
elif(10<=num and num<100):
    print("kétjegyű szám")
elif(100<=num and num<1000):
    print("háromjegyű szám")
else:
    print("A szám negatív vagy több mint háromjegyű")