from colored import *
def redNameFromConsole()-> str:
    name:str=None

    while(name==None or len(name)<2):
        print("Név:",end="")
        name = input()
        if(len(name) < 2):
            print("Nem megfelelő a név")
            
    return name.capitalize().strip()

def printWelcomeMessage(name : str)-> None:
    szam:int=len(name)
    print(f'%s Üdvözlöm  {name}%s' % (fg(szam), attr(0)))