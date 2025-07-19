name = input("What's your name? ")

match name:
    case "Harry" | "Hermoine" | "Ron": 
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")