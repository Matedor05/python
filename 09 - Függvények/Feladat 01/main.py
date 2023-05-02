from calendar import different_locale
from mathFunctions import *
from consoleIO import *


x: float = None
y: float = None
result: float = None


x = getNumberFromConsole()
y = getNumberFromConsole()

result = sumOfTwoNumbers(x, y)
printToConsole(x, y, result, "+")

result = differenceOfTwoNumbers(x, y)
printToConsole(x, y, result, "-")

result = multiplicationOfTwoNumbers(x, y)
printToConsole(x, y, result, "*" )

result = divisionOfTwoNumbers(x, y)
printToConsole(x, y, result, "/" )

