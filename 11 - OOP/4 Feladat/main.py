from videokartya import Videokartya
from processzor import Processzor
from computer import Pc
from tápegység import Tapegyseg

video: Videokartya = Videokartya()
video.gyarto = "Asus"
video.tipus = "RTX 3060"
video.fogyasztas = "650 W"

proci: Processzor = Processzor()
proci.gyarto = "Intel"
proci.tipus = "Intel Core i5-13600K"
proci.fogyasztas = "125 W"

tap: Tapegyseg = Tapegyseg()
tap.gyarto = "GIGABYTE"
tap.tipus = "GIGABYTE AORUS P750W"
tap.teljesitmeny = "750 W"

computer: Pc = Pc(video, proci, tap)
computer.tulajdonos = "Karasz Máté"

print(f"{computer}")

