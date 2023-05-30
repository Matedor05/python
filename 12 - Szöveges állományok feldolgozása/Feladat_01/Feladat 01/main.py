from typing import *
from student import Student
from studentIO import *
from services import *


# 1 - Írjuk ki minden diák adatát a képernyőre!
students: List[Student] = importStudents()
print("Az osztaly tanulói: ")
for student in students:
    print(student)

# 2 - Hány diák jár az osztályba?
countOfClass: int = len(students)
print(f"Az osztályba {countOfClass} tanuló jár\n\n")

# 3 - Mennyi az osztály átlaga?
classAvarage: float = calculateAvarage(students)
print(f"Az osztaly atlaga: {classAvarage:1.2f}")

# 4 - Keressük a legtöbb pontot elért érettségizőt és írjuk ki az adatait a képernyőre.
bestStudent: Student = getBestStudent(students)
print(f"Best student is : {bestStudent}")

# 5 - atlagfelett.txt allományba keressük ki azon tanulókat kiknek pontjai meghaladják az átlagot!
aboveAvarage:List[Student] = studentAboveAvarage(students,classAvarage)
writeStudentsInFile(aboveAvarage, "atlagfelett.txt")

# 6 - Van e kitünő tanulónk?
kituno:bool=studentKituno(students)
print(kituno)

# 7 - Hány elégtelen, elégséges, jó, jeles és kitünő tanuló van az osztályban?
#     Értékhatárok:
# 	- elégtelen, ha: 0.00 - 1.99
# 	- elégséges, ha: 2.00 - 2.99
# 	- jó, ha: 3.00 - 3.99
# 	- jeles, ha: 4.00 - 4.99
	# - kitünő, ha: 5.00

