# -*- coding: utf-8 -*-
"""BA1I.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ra0ZtuYmVoUqGxoetwRuGIoE4a7gcVoH
"""

def HammingDistance(p,q):
    n = len(p)
    counter = 0
    for i in range(0,n):
        if p[i] != q[i]:
            counter += 1
    return counter


def Neighbors(Pattern, d):
    
    if d == 0:
       return [Pattern]
    if len(Pattern) == 1:
        return ['A','C','G','T']

    neighborhood = []
    suffixNeighbors = Neighbors(Pattern[1:], d)

    for Text in suffixNeighbors:
        if HammingDistance(Pattern[1:], Text) < d:
            neighborhood.append('A'+Text)
            neighborhood.append('C'+Text)
            neighborhood.append('G'+Text)
            neighborhood.append('T'+Text)
        else:
            neighborhood.append(Pattern[0] + Text)
            
    return neighborhood


def NumberToSymbol(num):

    if num == 0:
        return "A"
    if num == 1:
        return "C"
    if num == 2:
        return "G"
    if num == 3:
        return "T"


def NumberToPattern(index,k):

    if k == 1:
        return NumberToSymbol(index)

    remainder = index % 4
    index = index // 4
    pattern = NumberToPattern(index,k-1) 
    return pattern + NumberToSymbol(remainder)


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


def FrequentWordsWithMismatchesBySorting(Text, k, d):

    FreqPatterns = []

    
    
   
    
    count = [0]*pow(4,k) 
    
    for i in range(0,len(Text)-k+1):

        
        
        
        neighbors = Neighbors(Text[i:i+k],d)
        
       
    
    
    
    
    
    
        for neighbor in neighbors:
            index = PatternToNumber(neighbor)
            count[index] += 1

    maxCount = max(count)

    for i in range(0, len(count)):
        
        if count[i] == maxCount:
            Pattern = NumberToPattern(i,k)
            FreqPatterns.append(Pattern)

    return FreqPatterns


def Output(array):

    out = ' '.join(array)
    print (out)


with open("rosalind_ba1i.txt") as file:
    lines = file.readlines()
array = FrequentWordsWithMismatchesBySorting(lines[0].strip("\n"),
                  int(lines[1].strip("\n").split(' ')[0]),
                  int(lines[1].strip("\n").split(' ')[1]))
Output(array)
