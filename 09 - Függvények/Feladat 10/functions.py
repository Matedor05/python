def getResult(randomNumber:int)->str:
    guess: int = None
    temp: str = None
    guessStr:float=None
    result: str = "Teli találat"
    while(guess!=randomNumber):
        print("Adja a tippét")
        temp = input()
        guessStr = temp.replace("-","").replace(".","")
        if(temp.isnumeric):
            guess=int(guessStr)
        else:
            print("Nem számot adott meg!")
            
        if(guess < randomNumber):
            print("A szám kisebb mint a véletlen szám")
        if(guess > randomNumber):
            print("A szám nagyobb mint a véletlen szám")
    return result
    
    