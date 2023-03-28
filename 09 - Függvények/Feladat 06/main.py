from consolIO import *
from function import *


mertekegyseg : str = None
temperature : int = None
mertekegyseg = getMertekegyseg()
temperature = getTemp()
result = getResult(mertekegyseg, temperature)
print(f"{result}")
