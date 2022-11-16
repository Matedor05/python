
zoldsegleves:bool=False
husleves:bool=False
gyumolcsleves:bool=False
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
else:
    print("Nem válsztott előételt")

sultcsirkecomb:bool=False
sultcsirkemell:bool=False
rakottzoldseg:bool=False
spagetti:bool=False
pizza:bool=False
foetel:int=None

foetel=int(input())

print("Válasszon főételt!")
print("1- Sültcsirkecomb")
print("2- Sült csirkemell")
print("3- Rakottzöldség")
print("4- Spagetti")
print("5- Pizza")

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
else:
    print("Nem válsztott főételt")


rizs:bool=False
paroltzoldseg:bool=False
gyumolcs:bool=False
sultkrumpli:bool=False
salata:bool=False
kola:bool=False
koret:int=None

print("Válasszon főételt!")
print("1- Rizs")
print("2- Pároltzöldség")
print("3- Gyümölcs")
print("4- Sültkrumpli")
print("5- Saláta")
print("6- Kóla")

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
else:
    print("Nem válsztott köretet")

print(f"Ön előételként {eloetel}-t, főételként {foetel}-t, köretként -t választott")