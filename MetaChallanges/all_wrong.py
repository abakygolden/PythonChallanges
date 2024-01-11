# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
    result = ""
    for index in range(N):
        character = C[index]
        if character == "A":
            result += "B"
        else:
            result += "A"
    return result;


print(getWrongAnswers(5, "BBBBB"))
