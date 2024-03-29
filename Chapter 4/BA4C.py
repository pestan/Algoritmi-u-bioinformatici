# -*- coding: utf-8 -*-
"""BA4C.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ra0ZtuYmVoUqGxoetwRuGIoE4a7gcVoH
"""

def CycloSpectrum(Peptide):
    AminoAcids = 'GASPVTCILNDKQEMHFRYW'
    Mass = [57,71,87,97,99,101,103,113,113,114,115,128,128,129,131,137,147,
            156,163,186]
    n = len(Peptide)
    Subpeptides=['']
    Spectrum=[0]
    for i in range(0,n):
        subpeptide = ''
        subpeptide_mass = 0
        for j in range(1,n):
            subpeptide += Peptide[(i+j)%n]
            index = AminoAcids.index(Peptide[(i+j)%n])
            subpeptide_mass += Mass[index]
            Spectrum.append(subpeptide_mass)
            Subpeptides.append(subpeptide)
    first_sub = Peptide[0]
    complement = Peptide[1:]
    index_first = Subpeptides.index(first_sub)
    index_comp =  Subpeptides.index(complement)
    mass_all = Spectrum[index_first] + Spectrum[index_comp]
    Spectrum.append(mass_all)
    Spectrum.sort()
    return Spectrum

def Output(array):
    out = ''
    for i in range(0,len(array)):
        out += str(array[i]) + ' '
    print(out)

with open("rosalind_ba4c.txt") as file:
    line = file.readline()
Output(CycloSpectrum(line.strip('\n')))