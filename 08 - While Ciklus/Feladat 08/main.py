temp:str=None
number:int=None
while(number==None):
    print("Adja meg az üdítő sorszámát")
    print("Coca Cola: 1")
    print("Sprite: 2")
    print("Fanta: 3")
    print("Gyümilé: 4")
    temp = input()
    if(temp.isnumeric()):
        number=int(temp)
match temp:
    case "1":
        print("Itt is a kóla")
    case "2":
        print("Itt is a sprite")
    case "3":
        print("Itt is a fanta")
    case "4":
        print("Itt is a gyümilé")

    