def getPayment(workerHours:int)->int:
    payment: int = None
    if(workerHours < 41):
        payment=workerHours*1000
    elif(workerHours >40):
        payment=(workerHours-40)*1500+workerHours*1000
    return payment
