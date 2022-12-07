ellenallas1:int=None
ellenallas2:int=None
kotes:str=None


print("Adjon meg két ellenállás értéket")
ellenallas1=int(input())
ellenallas2=int(input())
print("Adja meg milyen kötést szeretne létrehozni a két ellenállás között")
kotes=str(input().lower().strip())



match kotes:
    case "p":
        print((ellenallas1*ellenallas2)/(ellenallas1+ellenallas2))
    case "s":
        print(ellenallas1+ellenallas2)
   
