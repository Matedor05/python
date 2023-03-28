from functions import *
from functions2 import *
from consolIO import *

szoveg1: str = None
szoveg2: str = None
counter: int = None

szoveg1 = gettext()
szoveg2 = gettext()
counter = textCount(szoveg1, szoveg2)
print(counter)

