def getPenznem()-> str:
    temp: str = None
    while(temp == None):
        print("Adja meg milyen pénznembe szeretné átváltani pénzét: ")
        temp = input()
        return temp.lower().strip()

def getPenzMennyiseg()-> int:
    temp: str = None
    penz: int = None
    while(penz == None or penz < 1):
        print("Adja meg mennyi pénzt szeretne átváltani")
        temp = input()
        if (temp.isnumeric()):
            penz = int(temp)
    return penz
