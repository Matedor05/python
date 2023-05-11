class Telefon:
    
    def __init__(self):
        super().__init__()
        self.gyarto: str = "Xiaomi"
        self.modell: str = "Mi 11s"
        self.megjelenes: int = 2020
        self.akkumulator: int = 5000
        self.kijelzo: str = "IPS LCD"
        self.memoria: int = 6
        self.tarhely: int = 128
        self.kijelzoMeret: float = 6.3
        self.processzor: str = "Kirin 710"

    def kiratas(self) -> None:
        print(f"Gyarto: {self.gyarto}")

        