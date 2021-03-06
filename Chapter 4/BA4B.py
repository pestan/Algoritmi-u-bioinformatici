# -*- coding: utf-8 -*-
"""BA4B

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bUgf-grhJaNQTbwQEkhAI30hZrGNBRQC
"""

def kMers(text, k):
  kmers=[]
  for i in range(0, len(text), k):
    kmers.append(text[i:i+k])
  return kmers

first="ACGU"
second="ACGU"
third="UCAG"
letters="NNKKTTTTSSRRIIIMHHQQPPPPRRRRLLLLDDEEAAAAGGGGVVVVYY**SSSSCC*WFFLL"   # length(letters)=64
def Translate(abc):
  for i in range(0, 4):
    if (first[i]==abc[0]):
      br=i*16
  for i in range(0, 4):
    if (second[i]==abc[1]):
      br+=i*4
  for i in range(0, 4):
    if (third[i]==abc[2]):
      br+=i
  if (letters[br]=="*"):
    return ""
  else:
    return letters[br]

def Reverse(text):     # okrece rijec naopako
  reversed=""
  for i in range(1,len(text)+1):
    reversed+=text[-i]
  return reversed

def ReverseComplement(text):
  prijevod=""
  for slovo in text:
    if (slovo=="A"):
      prijevod+="T"
    if (slovo=="T"):
      prijevod+="A"
    if (slovo=="G"):
      prijevod+="C"
    if (slovo=="C"):
      prijevod+="G"
  return Reverse(prijevod)      # obrni redoslijed slova

def TuU(text):     # mijenja sva javljanja slova T sa slovom U
  prijevod=""
  for slovo in text:
    if (slovo=="T"):
      prijevod+="U"
    else:
      prijevod+=slovo
  return prijevod

def svi2kmeri(text,peptide):    # ako je peptid duljine 2 onda vraca sve podstringove duljine 6, jer u tekstu 3 slova daju jedno slovo peptida
  l=len(peptide)
  kmeri=[]
  for i in range(0,len(text)-l*3 + 1):
    kmeri.append(text[i:i+l*3])
  return kmeri

def PEP(text, peptide):          
  kmeri=svi2kmeri(text,peptide)     # daje sve podstringove duljine dvaput vece od duljine peptida
  substrings=[]
  l=len(kmeri[0])           # duljina svakog podstringa
  i=int(l/3)                # koliko odsjecaka u svakom podstringu imamo, tj. svaka 3 slova cine jedno slovo peptida
  for kmer in kmeri:
    pep=""
    for k in range(0,i):          # za svaki 3mer u tom kmeru gledamo oce li se on pretvorit u trazeno slovo peptida
      pep+=Translate(TuU(kmer[k*3:k*3+3]))
    if (pep==peptide):
      substrings.append(kmer)
    # sada za obrnute radimo isto:
    pep=""
    obrnut=ReverseComplement(kmer)
    for j in range(0,i):
      pep+=Translate(TuU(obrnut[j*3:j*3+3]))
    if (pep==peptide):
      substrings.append(kmer)
  for s in substrings:
    print (s)

PEP("ATCCCGGGTCCATTAAAGACACATCGTTGCCATCGACTCCGAAAGTACTTTGATAGACGCCTAATCGGACTATCGGACCAAGTTTCTGCCAACGGTCTCAATGCATCCGGTGGTTTCACGCCTCTTATTCCAATGAGAAGAGCGGCAGATCGAGCAACTAGTCGAAATTTGTTTTCATTGAGTTCTGAGAAAGTATTTTCAATGCGGATAGGTACCTATCGGCGTTCTCGTTGACTACCTTAGCAAGCTGGGGCATAGTTAAGGACTGCTATGCCGCACAGGCTGAGCACTCAAGTTACATCCAGATCACCACTCGCTTTTTGTTTATTACGGGCCATCATCCTACGGGAACAACCGAGGGTCAATTCTACCACCCGCGGAGGTGACTCTCCGATTGAGCACAAACTAGATAGGGTCGGGATAACGCATCCACTATTGATCACGTTGGCCAACCTGTCTCGAAGTAATGTATGATCTGTCCGCCACTACCCCACTCTACGGGTATGGTGCTCCCACATAGCAGGTAGAACCATGTCCACGGGCAGCCCAGCCCAGATCCTGATTGGACCACATGCCGAGGGAAACAAAGTTCCCTCGTCTTGTCGAATTGCAACCGGCACGATAATGCTATATAGGCAACAGGCTACCCGACACCGTCAAGCCAACGGCCTTACAGTCGTGATCACCATCATCGGGCGCGTAGTACCTGCCCGCCTTTATCCCTCGGTTTGTTATTCCGGTTGGATCGATTAGTCTTGCATGGAGCAACTTGCGGAACTACGGTTGGGGTCATACTATGTTCCACATTTCGACAGCAGTCACCGTACCGCAGGAAGCGTCCACGAGTTCAAAGCAGCGCTACTCTTTGGTTGGTCACCGGCGTCCAGGACATGGTTCTCCCGGCTATGTGGGAGTTTGCGATAAAGTGTCTTTTCCCCAAGGACCAGTCTACGCAGGCCCCGCAACCAACTAGTTGTCGCATGCAAGCGCTATCTATGGTATTAATAGAGCCTCGTAAAAATGGGCCGGCACTTACAATAATACGACTTGTATCGCCTGTCCTTAGGCATCATTCCGCTACTGCGCGGTTAGCAGTAAATGGTCCAAACAAGTGCGTTACTTGTATGTCGTGACTATGACATGGTATTGCCCGCGATGTGGGAGTTCTTCCGGAACTCTAAGGATGACGGTCTCACTTGAATACATTCCTCTGCTGTAGCGTTTCTTTGGGTGACCCGCGCCACCGGTTGATACGTAGTCGGAGTCAAATGTTCAGAGTCAGGGTAGCGTGTGACGAGATGCATGGGGTTGCTTTTGTCTTTCAGGCCGTTCAGGTGGCCAAGTCTGACTTCCGGGCATTTGACATGGTGCTGCCAGCCATGTGGGAAGATATACGGGCTAAACGCGTCGTATGCACACGAGTTCCCGGCGCGCCGATTGTGCGTGCCGACGAAAAAGAATCTATCTAATTCTACGCCTATAAATCTAGTCCTATTCAACCCCGGTAAAAAAGCGATAAATGGTCATCAACAAAAGGACGTGTACATAAATCGACAAGCCTCGCATGTCGCTAACGTAGCCCGAAAGAATATTCCTGGATATTCCCGACGGACCCCCTGGTCAACTTTATGCAATAACTCAGGGCACTGATCGTAGTGGTGGCGCCACATCGCTTTCGTTCACGTGTTTACGCCGATCGACCCGAGATTTGTCCCCTATGGGACCACGAGGAACAGGTCGTTACGTGCGAAATAAGTCAACTATGAAAGCCAAGCGGACTCCAATCGCGAGGTGAGACGGCCAAGGGGGTATTAAAAGAGACTAGGTGTCGCCGGTGCGTAAGAAAGTATCGCCGATGGCATACGCACATGGTGTCACAACCAGATCTGCGGACGTTAAGAGAGGACTAGATGCCATCCAAGACAACCAGCTCCTTGAGCTGTGGATACCTCCAAGGTTCGTAAGGGATCCTACTATGTGCAGGACCTACTCAACGACTTTATGCGATAGGTATAGGATGTAGGTGAGTTTGGTCATAACCTTAGACGTATACGGCCATGGATGCCATCAATACCTGGGGCGGGCGATCACTCCCACATCGCTGGGAGGACCATGTCTTTAACACGAAGACAAATCTAAGACATCTCTGGCAATGTACAGCACGCTGCTTAAGTCTCCAGAGATGAGATGAACATACGAAAGATCTTCACGACCTCTTGTTTCGCCAATCAGTTCAGATCAACCGGATCTATTATACGATTACGTAGGACGAGACTTTCTAGTTGGTCTCTTATAACCGCCCATCCGGACATATGGCTTTATACGGGCACCAGCTCTGCCCATCAAATGCAATTGAGAGGCACACCGTGAACTACCCCTATATTTACCCAAGACACGTACACCACTTAGAAATACGCATTCCCTGAGAAACATCAGCGGCCCCCAGATCACTACGGCTCGTGCTGCAGTTTCAAGCATTAATGACCATCGTTGTCCTCGCTACGCACAAGGATCTTGCCGGTTATCAAGTTGTTGACTAAAAAGCATCGGTATGTGGGAGGGTGTAATTCTCGCCCCCAAGTTGACTTTATAAGATATGGTACTACCCGCAATGTGGGAGTGAACAACCATTCGGTCGCAGTTCCTGATACATAACGAAGCAGTGCTTAGCAGTTGCATTAGGATCCTAAAGGGATCCTTCACGGCGCTAGTTTTGGGCGAAGTTAGTTTGACGCTCATATTAATTCTCTCCCAGACGTAGCCGAACAGACTTGCTAATCCAGGCTTGTGACACGGCCCTCATATGCCTAACTATATACGGTCTTCCCGTACTCTAGGGGCCATCTCCCCCGCCGAATGCAGTCCGAATAACACCATTTAAAATTATTGATCCACGGGTGCTTCTTTCAATATACACATAAGGTAGGCACTAGGAGATACCTTTAGATATGGTCCTGCCCGCAATGTGGGAAATTAGGCCAGGCGTACGGTTCCCTATTACGAGCGTATGTGCTAATGGTACCCGCTGAGACAGAAAAGGGGCCAGCCTACGAGATCTAGATTAAGAGGACAAAGGCGACTGTTTATCCGTGCGCCACCATTTCCTGAGAGGCTGTGAACGGGTCTGGATTCTGCGTAATACCGCAGTTAAGATTAGCTACAGTCGAAAATCCTGGTTCAACCGTTTGAAAGTGCCAGTATCCTCGTGTGGCCACTAATAACGCGAATGTTGTACTGAAGGTCTTGATGAGTATAACGGTGTAGGTTAGGCGTCTTCCGCGTACACAGTACTTTCGGGCGAGCTCGTGAAGAAAAGACTTTGTTGCATATCGGATCGATATATTCGCCGGAGTGTTTGGCTGCTGAGATGTACAGCATTGTCTTGTATCCGCTATTTGATCCGTGTCTGTGTATGCTGGTATACCTAGAATCCGATATTATAGCTCGCGACGGGCTGCGTCGGTTTAAGCTGCACCTACCGGACCTAGGGAGCCTCGAGCGATCTAAAGCGCCAGGCTGCGATATGGTGTTGCCGGCGATGTGGGAAGATGTGCCGCGGAATGTGATCCTCGTATGTAATCTAACATAGATCCGAACTTGTCCGTCGACTTATATGCGTTTACGTATAAGGACAACTTCGCTCGCCTCTTTCTCCTCTTATTAGATATATCTATGGCAAGTTCTCACGTGTGTTCACGGGTCGAGCGCCAAGGATACAACTTAATTAACTAAGAACCGTATGAGTCTATAATCGATCTGACTGCAGGTTAGTTCTTGCTAAATGGCTGGGCCGCTCTTCAGTAAAGGGCCTTCAACGTATCATTAACTCCGGCCTAAGGGGTTCTACCGTCGAAACTGGCGTTGGCGAACGCACTTGATATCAATAATTGTACATTCTCAGGATACGCTACCTTTCTAATCTCACCCCGGCTGACATGGTTCTGCCAGCAATGTGGGAAATCTTGGTGTATGACATACATGGACTAAGGACGCTCACCGGGGTGGACCTGCTCTCGGTAGGCGCCAGCACGTTTGTCGCGTGGTCACTAAGCCGATAATGTACCGGATAGGCAGTCTCATATCATCACGCCCATAAGGGGATGCACTAGCTTAGCAGGCCACCAAGAAAACGCTTGGTTACGCGCTAGCAAGACAATGTCTAAGATAACAGCATAGTTCGGATGGGCGTAAGGAGTACCAAAATGATCGTCGGCATTTCCTTTAACCAAAAGGCACCCCCGTAGTCGAAGGGGAGGCATACTTAGCCGAGGCAGGGTTCGATATGGTGCTGCCAGCGATGTGGGAATCTAACGAATGACAAGAGGGCTCATTTACGTGTCAAGCGCTTGTGGTGTGGTACCACTCTTAGGTGGATACATACTCTTCTGAACCTTTAGTTTGTTCTCTTACTCTATAGTTGCAAAATAGCGTAAGGGTAAGCACATGTGGCGTTTCTAGACGACCATTGTTGAAGTCTCCCACATTGCAGGTAGGACCATATCGGCGTTCACTTAGCGCAAACCGACATGGTTCTACCGGCCATGTGGGAGGGCCCGGAGAGATCTGTATTCCGTAGTAACTTCTACCACCCCATAGATTCTGTACTGAGAGGTAAGGAGGAAGCGTACTGAGATGGATGTCTGCATGCCTTAAGCAACTTCTTTCGGTCTATTACATACTGCGAGTGGGGTTGCGGGAGCGATATGTTGTGCGAGCCACTAAGACCATGAGATCCGGGTTAATGCATTCAGTCTTCCTATTTTGGTAACTATTCGAAGCGAATTACGTGCGCAGCGAATTTCGTAAAACGTCCGAGGAGCCATAGGAGTCTCTCCGTGTTTAATCTAACCAGGAGCGGCCGTGCCACATTGCCGAAATCGCGCCTATGGTTGACTTTCCTCTGTGCGAGATAAACCATAGGCGGAACTGACTCCCATTCCAAATGTTGAGATCACTGTCGCTACCTTCGAGACATAACTCTTTGGCTTCCGTCTCCTATTGGTCTTCTGTCCGGCTATAGCTGGGACACGTCTGTCCTGTCCCTCACAGTATACAACTAAAAGTGACAATTTCTACTGGTTTCCATCAATGATCCCTGTGGATAGAAATGTCCTAGCCGTTGATAATACGGACGCGCTCTACGCTAACACGCTGATCCCTCTTCACTCCAGAAGGAAAATATCGGCGTGCACGGCTAGGCTGCCCCGGTTTGACCATTGAGGCTTGTCCAACTCTTACAACGTAGAGCCGAGACATGGTACTACTCCCACATGGCGGGTAATACCATATCTCACGTCAATTTGATGTGTTAATAGCGTCTACCTCGCTACCTGTTCTTACCCGCGAAAGGCGGCTCAGTTCGGTCAACCTTGGTCAGACTAGCTCCAAATGGTTAGAACACGACAGAATGTAATAGAGCAGCTATTTTCAGGTTACCACTAAATACGCGAACTATCAGATCCGCAGGCGAGACGCACCCAATTGTTGGATAGCTCACGACACTAGGATCCGGCGGGTTCACCCTTCAGGAACTGGGTGCTTTTACTCCCACATGGCAGGAAGTACCATGTCTGGTCATTAGGACTTACAGCGGGCATCTTATTTCCCTCCCACATGGCAGGTAATACCATATCGGGAATGGGCGATCAACCCTACCAAGTGACATCCTGCATGGCGTGATATTATACCCACTATCAAGAAGTTTCTATGCCCTCAGGATCATCCCTACGGAATAAGACATGGTCCTGCCGGCAATGTGGGAAACGTCATCTCCACCTATAAATCTTTATACCTGTATGAGCGAATGTTCATAGTATGGCCAGTAAGTCTAGTTAACGGAAAGTGCAGAAGCTACTTGGACAAGTCTACGATCCCGCCCGCGGCATTACACGAACCATTTAGAGGTCTAGCCGAGATTACCGCATAAAAAGTATCCGCCCCGGAAGTCTCGGAGTAGTTCTACGGTCCAATCCCCAAGGGCCATGCGGCCAATCATAGCTCGAACTTGACATTGAGTATAAAATCCTCGCATTCGTCGTAATCGTCAACTGTATCCAGAGGACTGAGAACTCAAGACATTGTACGCTACGTTCGGATGTACTAGTTTATAACTATTAGATATTCTGGCGGACTCGGGCGGAGTCAGGTACAACCTACTCGGACTGCCGATCAGCTTTACCAGTGGGTAATTATTTCGAACACCCGTCTAGTATGGTGGAGGATAGGGGCCCACGTGCTCTGGCCGGGAATGCTTTCTTCGGGAGTCAAAACCCTTAGTGACCGATCATCGTGCGAGCACGACCAAGCGACCTGTTCATTCCAGAATCCGGTTTCTCGAGACCCGTGCGTCTAGTTTCATGGCGCGAACCAGAAACTAAGGCCTAGAGTAGTAGCGCACTACAAGATTGCGACCTCATGACATGTCATGGATAACGAGCACTCTCTGGGTCCCATACCCCCCGTTCCAACGGAACACCAGCGAATAGAGACGTGTCCAGTAAAACAAAGTAGGTCAGGCAGCCCTCAGCAGATGGCTTGCGCAAACCCGCCTTTACAACGGAACTAGCTGACCAAAATCAGGGATACCAGCATGTACAACTCCGGCGCATCAGGTCTGGTTTCAAAGATGGACCCCCCGTTATGCAACCACAGACTAATATCTGAGCGCGTCAGCAGCAAAACCAAGTTCTCTATGCCGGTTATGCTTTGACAGATGTATTTTTTAATCCCTGTTTTTCCTGCCCCTCGAAGGTTCGTATCACTGTGTATTCGGATGTGCTTAATATCAGTACGTGTATACTGACTTCCCAAAATCGACCGTGAGACTGATCCTATGAAGATCGTCTGCGGAGACACTACTTCGCATAGACCCGGGTTGGTCCTAAACTGAATGCTTCTCCCTCGGACGCCACTCGAGTAACCATGCAAGGTGTATCTTCTACTTCGTTCGGCTCACGTTTGGCGAAATTGCACGAGGAGCGATGGACTCCATTCCAGGACAAAAATAATTCGTGCAGCCGATTCAGTCCTGAATCACAACTGCGTGTAATCGACCAATCTTTTGCGTTCTCTACCGTATAGCTGGGGCACAAATGGAATTACTTCGTGTATACCAGCTAGTAGAATCATAGCGTTCCGGCCTATGTCAGCTCTACGGATCCTTAGGGGGACCATCGTCACCCCCCGGGCCGAACTCGCCAGGCGCATTGGAATCCCGGAAAAGGCACCAATATTACCAGACTCGTGTATGGCGACTATGACCTTACTCGGGCTCGAGCAGAAGCGCATGGCACGAGCTTCAGGAACGTGTGACTACCTGGACTTCGTGATGGACTGTAGACTCCGGAGATCGCGAACCCTGGCAACGAAGCGTGCCAAATGTTACGTGAGCCGGTGCTCGAACGACATGGTTTTGCCTGCAATGTGGGAGGGGTGTTTACTAGCAGATGTCAATCGGCCGTCTTAAAGAGCCTCTCGATGCCGTCATGTCTAGGCGTGATTCCGATACCATATGCTAGAGGTTTCCTATCGTTATTCGTTACGAGAATGCTACGGAAAGTCACCTGACTGCTAATTAACCGATTACGAGCAAGCCATGCTACAGTAGGGACCACACGGGAAATAGTAGGTAGGACTTACCGTAGTTCTCATAACCAAATCGCCGACTTAAAAATACGAACTTTTCCAGGTTCTTCTCGTGTGGTGCGCTAACGGTTTAAATTTCCATGCCATCGCTTCTTGCTGAACAATGCTAGTTGGACTCCCAGTGATGTTCTTCGTCCGCCGATCGTCTGTGTTAAGAGCTGACGAGAAGGTAACGTGAATAGGAAGACCCGATTGACTGTAGCGGAGCCAACCCTACTAGTGGGTGGGTACTCTATCGCAATTAATTTGGAGCGTCCACCTGTGCGCGATCTCGTTTACTGTGCAGTAAGGAAGTTTTTCATCGTAAGATGAGACCTGCAACCGACTAAATGCCCGAACGTAGGCAATGCGGGGGAATTTTAAGACTGTCGGAGGAGCTCCATATATCCTATTTAGCTCCGGTACCCGGTAGGGCTTTCTTGGGTCCATGTCGAGTGCGTATCCGGGTTTTTGGAAAATTGAGCTGATATCTCAATGCGGTCGAAGGATCGATGAGCCTAGCAGTAGAAATATAACCGCGCTTATCAGAGGAACATCACACGGTCTCGGCTACTTAGGATAATGTTGAAGGGTTGTGAGTTGAGACGATCTCCCACATAGCTGGCAACACCATGTCTGCCGGTAAGGCCACGAGTTTACGTTAATGGTTCACTTCTTTTTTGAGGAATGAAAGCCGCAGTTTTCTACGCTGCTAATCTAAAGCGGGCGGCGTTCGACCAGCTCCATACGACCGCGAGTAAAGGGTCTACAAAGAAAATGATATGGTGTTGCCTGCAATGTGGGAAATTGATTTGTGTAGTACATCTCACAATAGATAAGGTCTCCACTATCCACTCCACGGTATAAAATGGGAATGACTGCGAACA","DMVLPAMWE")

def PEP(text, peptide):
  kmeri=svi2kmeri(text,peptide)
  substrings=[]
  l=len(kmeri[0])
  i=int(l/3)
  for kmer in kmeri:
    pep=""
    for k in range(0,i):
      pep+=Translate(TuU(kmer[k*3:k*3+3]))
      #if (pep[k]!=peptide[k]):
        #break 
    if (pep==peptide):
      substrings.append(kmer)
    # sada za obrnute:
    pep=""
    obrnut=ReverseComplement(kmer)
    for j in range(0,i):
      pep+=Translate(TuU(obrnut[j*3:j*3+3]))
      #if (pep[j]!=peptide[j]):
        #break 
    if (pep==peptide):
      substrings.append(kmer)
  for s in substrings:
    print (s)