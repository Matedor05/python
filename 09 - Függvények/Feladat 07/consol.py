import random

def getList() -> str:
    list:str=""
    for i in range(0, 10):
        n = random.randint(0, 10)
        list += str(n) + ","
    return list

