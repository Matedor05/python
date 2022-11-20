
zoldsegleves:bool=None
husleves:bool=None
gyumolcsleves:bool=None
eloetel:int=None

print("Válasszon előételt!")
print("1- Zöldségleves")
print("2- Húsleves")
print("3- Gyümölcsleves")

eloetel=int(input())

if(eloetel==1):
    zoldsegleves=True
elif(eloetel==2):
    husleves=True
elif(eloetel==3):
    gyumolcsleves=True
    
    
    


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
elif(foetel==2):
    sultcsirkemell=True
elif(foetel==3):
    rakottzoldseg=True
elif(foetel==4):
    spagetti=True
elif(foetel==5):
    pizza=True
    
    
    
    
    
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
elif(koret==2):
    paroltzoldseg=True
elif(koret==3):
    gyumolcs=True
elif(koret==4):
    sultkrumpli=True
elif(koret==5):
    salata=True
elif(koret==6):
    kola=True


if(eloetel>0 and eloetel<4 and foetel>0 and foetel<6 and koret>0 and koret<7):
    if(zoldsegleves==True and spagetti==True and (salata==True or gyumolcs==True)and (pizza!=True and rakottzoldseg!=True)):
        print("Kiváló")
    elif(zoldsegleves==True and sultcsirkemell==True and sultkrumpli!=True and rizs==True):
        print("Fitnesz menü")
    elif(husleves==True and sultcsirkecomb==True and (sultkrumpli==True and salata==True) and (pizza!=True and rakottzoldseg!=True)):
        print("Vasárnapi menü")
    
