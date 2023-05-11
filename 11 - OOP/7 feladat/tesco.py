from udito import Udito
from chips import Chips
from muzli import Muzli

class Tesco():
    def __init__(self,chips:Chips,muzli:Muzli,udito:Udito)->None:
        super().__init__()
        self.chips = chips
        self.udito = udito
        self.muzli = muzli

    def __str__(self) -> str:
        return f"Tesco:\n\n{self.chips}\n\n{self.muzli}\n\n{self.udito}"