def readNameFromConsole() -> str:
    name: str = None
    while(name == None or len(name) < 2):
        print("Kérem adja meg a nevét!")
        name = input()

        if(len(name) < 2):
            print("Nem megfelelő a név")

    return name.capitalize().strip()

def birthDate() -> int:
    birthDate: int = None
    temp: str = None

    while(birthDate == None):
        print("Kérem adja meg mikor született!")
        temp = input()

        if (temp.isnumeric()):
            birthDate = int(temp)
        else:
            print("Ez nem év!")

    return birthDate

def printWelcomeMessage(name: str, age:int) -> None:
    print(f"Üdvözlöm {name}, Ön {age} éves")