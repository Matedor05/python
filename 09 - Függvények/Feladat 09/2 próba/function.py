def getEuro(huf:int)->float:
    euro: float = None
    euro=huf*0.0026
    return euro

def getResult(penznem:str, eur:int)->float:
    result: float = None
    match penznem:
        case "jpy":
            result=eur*0.75
        case "usd":
            result=eur*0.8
        case "chf":
            result=eur*0.55
    return result