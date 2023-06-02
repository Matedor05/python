from kezilabdas import *
from typing import *

def temaKereses(kezilabdasok:List[Kezilabdas],theme:str)->List[Kezilabdas]:
    utoJatekos:List[Kezilabdas]=[]
    for jatekos in kezilabdasok:
        if(jatekos.poszt == theme):
            utoJatekos.append(jatekos)
    return utoJatekos

def getMagassagszerint(kezilabdasok:List[Kezilabdas])->None:
    db:int=len(kezilabdasok)
    nagyobb:List[Kezilabdas]=[]
    for i in range(0,db-1,1):
        for j in range(i+1,db,1):
            if(kezilabdasok[i].magassag>kezilabdasok[j].magassag):
                nagyobb = kezilabdasok[i]
                kezilabdasok[i] = kezilabdasok[j]
                kezilabdasok[j] = nagyobb
