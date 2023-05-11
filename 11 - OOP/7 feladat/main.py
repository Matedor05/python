from chips import Chips
from muzli import Muzli
from udito import Udito
from tesco import Tesco

chips: Chips = Chips()
chips.gluten = "Tartalmaz"
chips.iz = "Paprika"
chips.nev = "Snack Day"
chips.tomeg = "200 g"

muzli: Muzli = Muzli()
muzli.gluten = "Tartalmaz"
muzli.iz = "Csokis"
muzli.nev = "Nesquik"
muzli.tomeg = "450 g"

udito: Udito = Udito()
udito.gluten = "Nem Tartalmaz"
udito.iz = "Alma"
udito.nev = "Sió"
udito.tomeg = "1 liter"


tesco: Tesco = Tesco(chips,muzli,udito)



print(tesco)

