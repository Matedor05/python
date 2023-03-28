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








overtime1=getOvertime(workerHours1, workerName1)
overtime2=getOvertime(workerHours2, workerName2)
overtime3=getOvertime(workerHours3, workerName3)
overtime4=getOvertime(workerHours4, workerName4)
overtime5=getOvertime(workerHours5, workerName5)

payment1=getPayment(overtime1)
payment2=getPayment(overtime2)
payment3=getPayment(overtime3)
payment4=getPayment(overtime4)
payment5=getPayment(overtime5)


print(f"{workerName1} ennyi {payment1} jár")
print(f"{workerName2} ennyi {payment2} jár")
print(f"{workerName3} ennyi {payment3} jár")
print(f"{workerName4} ennyi {payment4} jár")
print(f"{workerName5} ennyi {payment5} jár")







