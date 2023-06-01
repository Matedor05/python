from kezilabdas import *
from typing import *
import os
def fajlOlvasas()->List[Kezilabdas]:
    fajlnev:str= "data/adatok.txt"
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    teljesut:str=os.path.join(alaput,fajlnev)
    kezilabdasok:List[Kezilabdas]=[]
    egysor:str=None
    egyseg:List[str]=[]
    kezilabdas:Kezilabdas= None
    try:
        with open(teljesut,mode="r",encoding="utf-8") as file:
            for line in file:
                egysor =line.strip()
                egyseg=egysor.split("\t")
                kezilabdas = Kezilabdas()
                kezilabdas.csapat = egyseg[4]
                kezilabdas.magassag = int(egyseg[1])
                kezilabdas.nemzetiseg = egyseg[3]
                kezilabdas.nev = egyseg[0]
                kezilabdas.orszag = egyseg[5]
                kezilabdas.poszt = egyseg[2]
                kezilabdasok.append(kezilabdas)
            return kezilabdasok
    except FileNotFoundError as ex:
        print(f"{ex.filename} nem található!")
        return []

def fajlKiiras(kezilabdasok:List[Kezilabdas],fajlNev:str)->None:
    alaput:str=os.path.dirname(os.path.abspath(__file__))
    alaput += "/output/"
    teljesUt:str=os.path.join(alaput,fajlNev)
    # try:
    with open(teljesUt,encoding="utf-8",mode="w",) as file:
        for jatekosok in kezilabdasok:
            file.write(f"{jatekosok}\n")
        
    # except FileNotFoundError as ex:
    #     print(f"{ex.filename} fájlal valami nyűg van")