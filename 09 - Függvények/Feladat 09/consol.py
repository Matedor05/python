def getHuf() -> int:
    hufStr: str = None
    huf: int = None
    while(huf==None):
        print("Adja meg mennyi pénzt szeretne átváltani")
        hufStr=input()
        if(hufStr.isnumeric):
            huf=int(hufStr)
    return huf



def getPenznem() -> str:
    penznem : str = None
    while(penznem==None):
        print("Kérem adja meg milyen pénznemet szeretne:\nUsa dollár:[usd]\nSvájci frank[chf]\nJapán jen: [jpy]")
        penznem = input()
    return penznem.strip().capitalize().lower()