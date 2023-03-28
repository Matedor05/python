from unicodedata import name


def gettext()-> str:
    text:str=None

    while(text==None):
        print("Szöveg:",end="")
        text = input()
    return text
