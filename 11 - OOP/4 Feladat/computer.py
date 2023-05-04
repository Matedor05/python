from videokartya import Videokartya
from processzor import Processzor
from tápegység import Tapegyseg
class Pc():
    def __init__(self,videokartya:Videokartya,processzor:Processzor,tapegyseg:Tapegyseg)->None:
        super().__init__()
        self.tulajdonos = None
        self.videokartya = videokartya
        self.processzor = processzor
        self.tapegyseg = tapegyseg


    def __str__(self) -> str:
        return f"Tulajdonos: {self.tulajdonos}\n\nVideokártya:\nGyártó: {self.videokartya.gyarto}\nTípus: {self.videokartya.tipus}\nFogyasztás: {self.videokartya.fogyasztas}\n\nProcesszor:\nGyártó:{self.processzor.gyarto}\nTípus: {self.processzor.tipus}\nFogyasztás: {self.processzor.fogyasztas}\n\nTápegység:\nGyártó:{self.tapegyseg.gyarto}\nTípus: {self.tapegyseg.tipus}\nFogyasztás: {self.tapegyseg.teljesitmeny}"