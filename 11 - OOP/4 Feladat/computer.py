from videokartya import Videokartya
from processzor import Processzor
class Pc():
    def __init__(self,videokartya:Videokartya,processzor:Processzor)->None:
        super().__init__()
        self.tulajdonos = None
        self.videokartya = videokartya
        self.processzor = processzor


    def __str__(self) -> str:
        return f"Tulajdonos: {self.tulajdonos}\nVideokártya:\nGyartó: {self.videokartya.gyarto}\nTípus: {self.videokartya.tipus}\nFogyasztás: {self.videokartya.fogyasztas}\nProcesszor:\nGyarto:{self.processzor.gyarto}"