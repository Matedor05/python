def getResult(penznem:str, huf:int)->float:
    result : float = 0
    if(penznem == "jpy"):
        result=huf*0.37
    elif(penznem  == "chf"):
        result=huf*0.0026
    elif(penznem  == "usd"):
        result=huf*0.0028
    return result

def getEuro(penznem:str, huf:int)->float:
    euro: float = None
    euro=380
    return euro