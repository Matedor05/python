def getResult(mertekegyseg:str, temperature:int)->float:
    result : float = 0
    if(mertekegyseg == "K"):
        result+=temperature+273
    if(mertekegyseg  == "F"):
        result=9/5*temperature+32
    return result
