

class Tolltarto():
    def __init__(self)->None:
        super().__init__()
        self.radir:str = None
        self.toll:str = None
        self.ceruza:str = None
        self.hibajavító:str = None
        self.tollakSzama:int =  0

    def __str__(self) -> str:
        return f"Radír: {self.radir}\nToll: {self.toll}\nCeruza: {self.ceruza}\nHibajavító: {self.hibajavító}\nTollak szama: {self.tollakSzama}\n"