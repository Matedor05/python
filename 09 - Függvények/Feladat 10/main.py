from consol import *
from functions import *

number1: int = None
number2: int = None
randomNumber: int = None
result: str = None

number1=getNumber1()
number2=getNumber2()
randomNumber=getRandom(number1, number2)
result=getResult(randomNumber)
print(number1)
print(number2)
print(randomNumber)
print(result)