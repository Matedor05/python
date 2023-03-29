from consol import *
from function import *

huf: int = None
huf=getHuf()

penznem: str = None
penznem=getPenznem()

result:float= None
result = getResult(penznem, huf)

euro: float = None
euro=getEuro(penznem, result)



print(f"A megadott összeg ennyinek felel meg {penznem}-ben{result}")
print(f"A megadott összeg ennyinek felel meg euróban:{euro}")

