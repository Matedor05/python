szam1:int=None
szam2:int=None
eredmeny:int=None

print("Adjon meg egy számot: ",end='')
szam1=int(input())
print("Adjon meg egy másik számot: ",end='')
szam2=int(input())
eredmeny=szam1+szam2
for eredmeny in range(szam1, szam2, 1):
    print(eredmeny)