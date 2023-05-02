def getTemp() -> int:
    temp : str = None
    temperature:int=None
    while(temp == None):
        print("Kérem adja meg hány fok van (Celsiusban):")
        temp=input()
        if(temp.isnumeric):
            temperature=int(temp)
    return temperature


def getMertekegyseg() -> str:
    mertekegyseg : str = None
    while(mertekegyseg==None or len(mertekegyseg)>=2):
        print("Kérem adja meg milyen mértékegységet szeretne:\nKelvin:[K]\nFahrenheit[F]")
        mertekegyseg = input()
    return mertekegyseg.upper()


