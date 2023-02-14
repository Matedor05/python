
zoldsegleves:bool=None
husleves:bool=None
gyumolcsleves:bool=None
eloetel:int=None
menu:str=("A mai menü tartama: ")
ertekeles:str=("")




print("Válasszon előételt!")
print("1- Zöldségleves")
print("2- Húsleves")
print("3- Gyümölcsleves")

eloetel=int(input())

if(eloetel==1):
    zoldsegleves=True
    menu+="Zöldségleves, "
elif(eloetel==2):
    husleves=True
    menu+="Húsleves, "
elif(eloetel==3):
    gyumolcsleves=True
    menu+="Gyümölcsleves, "

    
    
    


sultcsirkecomb:bool=None
sultcsirkemell:bool=None
rakottzoldseg:bool=None
spagetti:bool=None
pizza:bool=None
foetel:int=None
    
print("Válasszon főételt!")
print("1- Sültcsirkecomb")
print("2- Sült csirkemell")
print("3- Rakottzöldség")
print("4- Spagetti")
print("5- Pizza")

foetel=int(input())

if(foetel==1):
    sultcsirkecomb=True
    menu+="Sültcsirkecomb, "
elif(foetel==2):
    sultcsirkemell=True
    menu+="Sült csirkemell, "
elif(foetel==3):
    rakottzoldseg=True
    menu+="Rakottzöldség, "
elif(foetel==4):
    spagetti=True
    menu+="Spagetti, "
elif(foetel==5):
    pizza=True
    menu+="Pizza, "
    
    
    
    
    
rizs:bool=False
paroltzoldseg:bool=None
gyumolcs:bool=None
sultkrumpli:bool=None
salata:bool=None
kola:bool=None
koret:int=None

print("Válasszon köretet!")
print("1- Rizs")
print("2- Pároltzöldség")
print("3- Gyümölcs")
print("4- Sültkrumpli")
print("5- Saláta")
print("6- Kóla")

koret=int(input())

if(koret==1):
    rizs=True
    menu+="Rizs, "    
elif(koret==2):
    paroltzoldseg=True
    menu+="Pároltzöldség, "    
elif(koret==3):
    gyumolcs=True
    menu+="Gyümölcs, "    
elif(koret==4):
    sultkrumpli=True
    menu+="Sültkrumpli, "    
elif(koret==5):
    salata=True
    menu+="Saláta, "   
elif(koret==6):
    kola=True
    menu+="Kóla, "   


if(eloetel>0 and eloetel<4 and foetel>0 and foetel<6 and koret>0 and koret<7):
    if(zoldsegleves==True and spagetti==True and (salata==True or gyumolcs==True)and (pizza!=True and rakottzoldseg!=True)):
        ertekeles+="A mai menü értékelése: Kiváló"
    elif(zoldsegleves==True and sultcsirkemell==True and sultkrumpli!=True and rizs==True):
        ertekeles+="A mai menü értékelése: Fitnesz menü"
    elif(husleves==True and sultcsirkecomb==True and (sultkrumpli==True and salata==True) and (pizza!=True and rakottzoldseg!=True)):
        ertekeles+="A mai menü értékelése: Vasárnapi menü"
    elif(pizza==True or spagetti==True and kola==True and (rakottzoldseg!=True and paroltzoldseg!=True)):
        ertekeles+="A mai menü értékelése: Napi menü"

    
print(menu)
print(ertekeles)