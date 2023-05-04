from videokartya import Videokartya
from processzor import Processzor
class Pc():
    def __init__(self)->None:
        super().__init__()
        self.tulajdonos = None
        self.videokartya = None
        self.processzor = None


    def __str__(self) -> str:
        return f"Tulajdonos: {self.tulajdonos}\nVideokártya:\nGyartó: {self.videokartya.gyarto}\nTípus: {self.videokartya.tipus}\nFogyasztás: {self.videokartya.fogyasztas}\nProcesszor:\nGyarto:{self.processzor.gyarto}"