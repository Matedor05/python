def getResult(sum1:int, sum2:int)->str:
    result: str = ""
    if(sum1 > sum2):
        result="Az első halmaz a nagyobb"
    if(sum1 > sum2):
        result="A második halmaz a nagyobb"
    if(sum1 > sum2):
        result="A a két halmaz összege egyewnlő"
    return result


    


def listSum(halmaz1:str)->int:
    sum: int = 0
    for number in halmaz1:
        sum+=int(number)
    return sum