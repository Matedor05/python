from videokartya import Videokartya
from processzor import Processzor
from computer import Pc

video: Videokartya = Videokartya()
video.gyarto = "Asus"
video.tipus = "RTX 3060"
video.fogyasztas = "650 W"

proci: Processzor = Processzor()
proci.gyarto = "Intel"
proci.tipus = "Intel Core i5-13600K"
proci.fogyasztas = "125 W"

computer: Pc = Pc(video, proci)
computer.tulajdonos = "Karasz Máté"
print(f"{computer}")

