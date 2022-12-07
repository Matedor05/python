drink:int=None

print("Adja meg az üdítő sorszámát")

drink=int(input())

match drink:
    case 1:
        print("Coca Cola")
    case 2:
        print("Pepsi")
    case 3:
        print("Fanta")
    case 4:
        print("Sprite")