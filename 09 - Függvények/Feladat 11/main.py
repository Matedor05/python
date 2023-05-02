from consoleIO import *
from helpers import *

workerName1: str = getName()
workerHours1: int = getHours()

workerName2: str = getName()
workerHours2: int = getHours()

workerName3: str = getName()
workerHours3: int = getHours()

workerName4: str = getName()
workerHours4: int = getHours()

workerName5: str = getName()
workerHours5: int = getHours()


payment1=getPayment(workerHours1)
payment2=getPayment(workerHours2)
payment3=getPayment(workerHours3)
payment4=getPayment(workerHours4)
payment5=getPayment(workerHours5)


print(f"{workerName1} ennyi a heti fizetése: {payment1} ")
print(f"{workerName2} ennyi a heti fizetése: {payment2} ")
print(f"{workerName3} ennyi a heti fizetése: {payment3} ")
print(f"{workerName4} ennyi a heti fizetése: {payment4} ")
print(f"{workerName5} ennyi a heti fizetése: {payment5} ")







