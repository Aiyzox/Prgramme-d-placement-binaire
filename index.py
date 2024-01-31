binaryNumber = input("Enter le nombre binaire : ")
directions = [binaryNumber[i:i+2] for i in range(0, len(binaryNumber), 2)]
result = ""
invalidSyntax = False
for direction in directions:
    match direction:
        case "00":
            result += "h"
        case "01":
            result += "b"
        case "10":
            result += "d"
        case "11":
            result += "g"
        case _:
            invalidSyntax = True
if invalidSyntax == True:
    print("Syntaxe invalide")
else:
    print(result)
    position = [0, 0]
    for direction in result:
        match direction:
            case "h":
                position[1] += 1
            case "b":
                position[1] -= 1
            case "d":
                position[0] += 1
            case "g":
                position[0] -= 1
    print("Position finale :", position)