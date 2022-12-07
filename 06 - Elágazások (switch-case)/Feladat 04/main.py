num1:int=None
num2:int=None
operation:str=None
result:float=None

print("Adjon meg két számot és egy műveletet")
num1=int(input())
num2=int(input())
operation=str(input())



match operation:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)     
