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

computer: Pc = Pc()
computer.tulajdonos = "Karasz Máté"
computer.videokartya = videokartya.
computer.processzor = Processzor()

print(f"{computer}")

