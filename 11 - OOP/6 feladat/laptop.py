

class Laptop():
    def __init__(self)->None:
        super().__init__()
        self.kijelzo:str = None
        self.processzor:str = None
        self.memoria:str = None
        self.videokartya:str = None
        self.tarhely:int =  0

    def __str__(self) -> str:
        return f"Kijelzo: {self.kijelzo}\nProcesszor: {self.processzor}\nMemória: {self.memoria}\nVideokártya: {self.videokartya}\nTárhely: {self.tarhely}\n"