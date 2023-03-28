def textCount(szoveg1 : str, szoveg2 : str )->int:
    counter  :int = 0
    matches : str = ""
    for i in szoveg1:
        if(szoveg2.find()>i and matches.find(i)==0):
                matches += i
    return counter
