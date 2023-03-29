from consol import *
from function import *

huf: int = None
huf=getHuf()

penznem: str = None
penznem=getPenznem()

euro: float = None
euro=getEuro(huf)

result: float = None
result=getResult(penznem, euro)

print(f"A megadott összeg ennyinek felel meg euróban: {euro:1.2f}")
print(f"A megadott összeg ennyinek felel meg {penznem}-ben: {result:1.2f}")
