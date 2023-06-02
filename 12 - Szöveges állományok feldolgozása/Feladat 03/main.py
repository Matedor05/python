from kibe import *
from kezilabdas import *
from functions import *

# - Írjuk ki a képernyőre az össz adatot
Kezilabdasok:List[Kezilabdas]=fajlOlvasas()
for kezilabdas in Kezilabdasok:
    print(kezilabdas)

# - Keressük ki az ütő játékosokat az utok.txt állömányba
utoJatekos:List[Kezilabdas]=temaKereses(Kezilabdasok ,"ütő")
fajlKiiras(utoJatekos,"utok.txt")

# - A csapattagok.txt állományba mentsük a csapatokat és a hozzájuk tartozó játékosokat a következő formában:
getMagassagszerint(Kezilabdasok)
fajlKiiras(getMagassagszerint,"magaslatok.txt")

# - Rendezzük a játékosokat magasság szerint növekvő sorrendbe és a magaslatok.txt állományba mentsük el.

# - Mutassuk be a nemzetisegek.txt állományba, hogy mely nemzetiségek képviseltetik magukat a röplabdavilágban mint játékosok és milyen számban.
# - atlagnalmagasabbak.txt állományba keressük azon játékosok nevét és magasságát akik magasabbak mint az „adatbázisban” szereplő játékosok átlagos magasságánál.
# - Állítsa növekvő sorrendbe a posztok szerint a játékosok ösz magasságát
# - Egy szöveges állományba, „alacsonyak.txt” keresse ki a játékosok átlagmagasságától alacsonyabb játékosokat. Az állomány tartalmazza a játékosok nevét,  magasságát és hogy mennyivel alacsonyabbak az átlagnál, 2 tizedes pontossággal.