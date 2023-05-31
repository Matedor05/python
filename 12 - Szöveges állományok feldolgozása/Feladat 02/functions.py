from konyv import *
from typing import *

def temaKereses(konyvek:List[Konyv],theme:str)->List[Konyv]:
    infosKonyvek:List[Konyv]=[]
    for konyv in konyvek:
        if(konyv.tema == theme):
            infosKonyvek.append(konyv)
    return infosKonyvek

def evjaratSzamitas(konyvek:List[Konyv],start:int,end:int )->List[Konyv]:
    megfeleloEvjarat:List[Konyv]=[]
    for konyv in konyvek:
        if(int(konyv.kiadvasiEv) >=start and int(konyv.kiadvasiEv) <end):
            megfeleloEvjarat.append(konyv)
    return megfeleloEvjarat
