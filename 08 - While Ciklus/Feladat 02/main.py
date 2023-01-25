name:str=None
temp:str=None

while(name==None):
    print("Adja meg a nevét:",end="")
    temp = input().strip()
    if(len(temp)>=2 and temp.isalpha()):
        name=temp