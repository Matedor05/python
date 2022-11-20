zoldsegleves:bool=None
husleves:bool=None
gyumolcsleves:bool=None
sultcsirkecomb:bool=None
sultcsirkemell:bool=None
rakottzoldseg:bool=None
spagetti:bool=None
pizza:bool=None
rizs:bool=False
paroltzoldseg:bool=None
gyumolcs:bool=None
sultkrumpli:bool=None
salata:bool=None
kola:bool=None
koret:int=None

zoldsegleves2:int=None
husleves2:int=None
gyumolcsleves2:int=None
sultcsirkecomb2:int=None
sultcsirkemell2:int=None
rakottzoldseg2:int=None
spagetti2:int=None
pizza2:int=None
rizs2:int=None
paroltzoldseg2:int=None
gyumolcs2:int=None
sultkrumpli2:int=None
salata2:int=None
kola2:int=None

print("Adja meg mit szeretne 1=igen 2=nem!")
print("zoldsegleves[i]:")
zoldsegleves2=int(input())
if(zoldsegleves2==2):
    zoldsegleves==True

print("huslevesleves[i]:")
husleves2=int(input())

print("gyumolcsleves[i]:")
gyumolcsleves2=int(input())

print("sultcsirkecomb[i]:")
sultcsirkecomb2=int(input())

print("sultcsirkemell[i]:")
sultcsirkemell2=int(input())

print("rakottzoldseg[i]:")
rakottzoldseg2=int(input())

print("spagetti[i]:")
spagetti2=int(input())

print("pizza[i]:")
pizza2=int(input())

print("paroltzoldseg[i]:")
paroltzoldseg2=int(input())

print("gyumolcs[i]:")
gyumolcs2=int(input())

print("sultkrumpli[i]:")
sultkrumpli2=int(input())

print("salata[i]:")
salata2=int(input())

print("kola[i]:")
kola2=int(input())

if(zoldsegleves==True and husleves==True):
    print("kiváló")
elif(zoldsegleves==True or husleves!=True):
    print("")


