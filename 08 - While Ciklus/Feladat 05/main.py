

temp2:str=None
temp:int=0
number:int=None
osszeg:int=0
db:int=0
limit:int=None
limit: int = None

while(limit == None or not isinstance(limit, int)):
        print("Limit: ", end="")
        temp2 = input().strip()
        temp2 = temp2.replace(".", "").replace("-", "")
        if(temp2.isnumeric):
            limit = int(temp2)


while(number==None or number < limit):
    print("Adjon meg egy számot")
    temp= input()
    if (temp.isnumeric()):
        number=int(temp)
    else:
        continue
    osszeg+=number
    db+=1
    print(f"A számok összege: {osszeg}")

if(osszeg>=limit):
    print(f"{db} lépésben érte el a limitet-et")