x:float=None
y:float=None
z:float=None

print("Adjon meg három számot")
x=float(input())
y=float(input())
z=float(input())

if(x % y ==0 and x % z ==0):
    print("Az x osztható y-al és z-el is")
elif(x % y ==0 and x % z !=0):
    print("Az x csak az y-al osztható")
elif(x % y !=0 and x % z ==0):
    print("Az x csak az z-el osztható")
else:
    print("Nem osztható sem y-al sem z-el")