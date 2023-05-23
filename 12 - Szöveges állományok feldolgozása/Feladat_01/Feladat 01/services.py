from typing import *
from student import Student


def calculateAvarage(students: List[Student])->float:
    sum: float = 0
    
    for student in students:
        sum += student.avarage
    return sum / len(students)

def getBestStudent(students: List[Student])->Student:
    bestStudent: Student = students[0] #referencia ertek
    for index in range(1, len(students),1):
        if(students[index].avarage > bestStudent.avarage):
            bestStudent = students[index]
    return bestStudent

def studentAboveAvarage(students: List[Student],classAvarage:float)->List[Student]:
    aboveAvarage:List[Student] = []

    for student in students:
        if(student.avarage>= classAvarage):
            aboveAvarage.append(student)

    return aboveAvarage

def studentKituno(students: List[Student])->str:
    kituno:str=None
    for student in students:
        while(student.avarage!=5 or kituno==None):
            kituno=="Van"
        else:
            kituno=="Nincs"
    return kituno
            
