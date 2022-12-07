import math
a:int=None
b:int=None
ertekek:str=None


print("Adja meg a téglalap oladalainak hosszát és hogy mit szeretne kiszámolni")
a=int(input())
b=int(input())
ertekek=str(input().lower().strip())



match ertekek:
    case "k":
        print(2*(a+b))
    case "t":
        print(a*b)
    case "e":
        print(math.pow(a)*math.pow(a))