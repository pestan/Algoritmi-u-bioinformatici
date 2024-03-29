# -*- coding: utf-8 -*-
"""BA1N.ipynb

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

def Output(array):
    out = ''
    for element in array:
        out += element + '\n'
    print (out)

with open("rosalind_ba1n.txt") as file:
    lines = file.readlines()
array = Neighbors(lines[0].strip("\n"), int(lines[1].strip("\n")))
Output(array)