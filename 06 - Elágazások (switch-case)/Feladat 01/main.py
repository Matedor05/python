from unittest import case


day:str=None
print("Milyen nap van ma? ")
day=str(input().lower().strip())

match day:
    case "hétfő":
       print("Hétfő")
    case "kedd":
        print("Kedd")
    case "szerda":
        print("Szerda")
    case "csütörtök":
        print("Csütörtök")
    case "péntek":
       print("Péntek")
    case "szombat":
        print("Szombat")
    case "vasárnap":
        print("Vasárnap")






