class Udito():
    def __init__(self)->None:
        super().__init__()
        self.tomeg:str = None
        self.iz:str = None
        self.gluten:str = None
        self.nev:str = None
    def __str__(self) -> str:
        return f"Üdítő:\n{self.nev}\n Ürtartalom: {self.tomeg}\n Íz: {self.iz}\n Glutén: {self.gluten}"