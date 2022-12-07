ellenallas1:int=None
ellenallas2:int=None
kotes:str=None


print("Adjon meg két ellenállás értékét és a kötést")
ellenallas1=int(input())
ellenallas2=int(input())
kotes=str(input())



match kotes:
    case "P":
        print((ellenallas1*ellenallas2)/(ellenallas1+ellenallas2))
    case "S":
        print(ellenallas1+ellenallas2)
   
