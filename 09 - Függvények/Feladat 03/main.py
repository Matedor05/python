from consolIO import *
from ageCalc import *

name: str = readNameFromConsole()
age: int = yourAge()

printWelcomeMessage(name, age)