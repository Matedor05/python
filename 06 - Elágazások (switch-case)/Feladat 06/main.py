import math
a:int=None
b:int=None
ertekek:str=None


print("Adjon meg két ellenállás értékét és a kötést")
a=int(input())
b=int(input())
ertekek=str(input())



match ertekek:
    case "kerület":
        print(2*(a+b))
    case "terület":
        print(a*b)
    case "átló":
        print(math.pow(a)*math.pow(a))