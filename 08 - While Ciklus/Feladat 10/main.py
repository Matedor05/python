temp:str=None
number:int=None
osszeg:int=0
osztas:int=0
osztas2:int=0
while(number==None or number<9 or number>100 or number%2!=0):
    print("Adjon meg egy kétjegyű pozitív számot!")
    temp=input()
    if(temp.isnumeric):
        number=int(temp)
print("0 és n közötti számok:")
for i in range(0 , number+1 ,2):
    print(i)
print('0 és n közötti számok összege')
for j in range(0 , number+1 ,1):
    osszeg+=j
print(osszeg)
print("11 osztható számok darabszáma")
for k in range(1 , number+1 ,1):
    if(k%11==0):
        osztas+=1
print(osztas)
print("7-tel 3 madékot ado számok")
for l in range(1 , number+1 ,1):
    if(l%7==3):
        print(l)

