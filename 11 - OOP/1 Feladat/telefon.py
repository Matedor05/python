class Telefon:
    def __init__(self, gyarto:str):
        super().__init__()
        self.gyarto = gyarto
       # self.modell = 
        #self.megjelenes = 
       # s#elf.akkumulator = 
       # self.kijelzo = 
       # self.kijelzoMeret = 
      #  self.processzor = 
       # self.memoria = 
       # self.tarhely = 
    
    def kiiras(self) -> None:
        print(f"Gyarto: {self.gyarto}")

    # Modell: {self.modell}\nMegjelenés: {self.megjelenes}\nAkkumulátor: {self.akkumulator}\nKijelző: {self.kijelzo}\nKijelzőméret: {self.kijelzoMeret}\nProcesszor: {self.processzor}\nMemória: {self.memoria}\nTarhely: {self.tarhely} ")