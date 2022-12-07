from unittest import case


day:int=None
print("Melyik hónap van?")
month =str(input().lower().strip())

match month:
    case "január":
       print("Január van")
    case "február":
        print("Február van")
    case "március":
       print("Március van")
    case "április":
        print("Április van")
    case "május":
       print("Május van")
    case "június":
        print("Június van")
    case "július":
       print("Július van")
    case "augusztus":
        print("Augusztus van")
    case "szeptember":
       print("Szeptember van")
    case "október":
        print("Október van")
    case "november":
       print("November van")
    case "december":
        print("December van")