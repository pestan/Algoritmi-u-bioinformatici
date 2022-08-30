def SymbolToNumber(symbol):

    if symbol == "A":
        return 0
    elif symbol == "C":
        return 1
    elif symbol == "G":
        return 2
    elif symbol == "T":
        return 3


def PatternToNumber(Pattern):

    if Pattern == "":
        return 0

    symbol = Pattern[len(Pattern)-1]
    prefix = Pattern[0:len(Pattern)-1]
    return 4*PatternToNumber(prefix) + SymbolToNumber(symbol)


def FrequencyArray(Text,k):

    frequency = [0]*pow(4,k)
    out = ""

    for i in range (0,len(Text) - k + 1):
        frequency[PatternToNumber(Text[i:i+k])] += 1

    for element in frequency:
        out += str(element) + " "

    return out

    
with open("rosalind_ba1k.txt") as file:
    lines = file.readlines()
print(FrequencyArray(lines[0].strip("\n"),int(lines[1].strip("\n"))))
