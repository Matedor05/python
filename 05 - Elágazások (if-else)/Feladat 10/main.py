num1:int=None

print("Adjon meg egy számot")
num1=int(input())

if(num1% 2==0 and num1% 3!=0):
    print("BIZ")
elif(num1% 3==0 and num1% 2!=0):
    print("BAZ")
elif(num1% 3==0 and num1% 2==0):
    print("ZIZI")
else:
    print(":(")
