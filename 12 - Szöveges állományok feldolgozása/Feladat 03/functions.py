from kezilabdas import *
from typing import *

def temaKereses(kezilabdasok:List[Kezilabdas],theme:str)->List[Kezilabdas]:
    utoJatekos:List[Kezilabdas]=[]
    for jatekos in kezilabdasok:
        if(jatekos.poszt == theme):
            utoJatekos.append(jatekos)
    return utoJatekos