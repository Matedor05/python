num1:int=None

print("Adjon meg egy számot")
num1=int(input())


if(num1% 6==0 and num1% 4==0):
    print("osztható 6-tal és 4-gyel")
elif(num1% 6==1 or num1% 4==0):
    print("osztható 4-gyel")
elif(num1% 6==0 or num1% 4==1):
    print("osztható 6-tal")
else:
    print("6-tal és 4-gyel sem osztható")
