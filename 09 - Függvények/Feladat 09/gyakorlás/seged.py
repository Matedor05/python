temp: str = None
penz: int = None
while(penz == None or penz < 1):
    print("Adja meg mennyi pénzt szeretne átváltani")
    temp = input()
    if (temp.isnumeric()):
        penz = int(temp)
    else:
        print("Nem számot adott meg!")
print(penz)
