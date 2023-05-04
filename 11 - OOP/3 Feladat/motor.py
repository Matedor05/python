class Motor():
    def __init__(self)->None:
        super().__init__()
        self.model:str=None
        self.manufacturer:str=None
        self.type:str=None
        self.horsePower:int=0
        self.cylinders:int=0
        self.fuelConsuption:int=0
        self.productionYear:int=0
        self.torgue:int=0
    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}{self.productionYear}"
