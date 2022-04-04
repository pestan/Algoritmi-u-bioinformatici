def kmer(text, i, k):
    return text[i: i+k]


def frequentwords(text,k):
    D=dict()
    lista=[]
    for i in range(0, len(text)-k+1):
        word=kmer(text, i, k)
        try:
            D[word]=1
            lista.append(word)
        except KeyError:
            D[word]=1
    max=0
    mostfrq=set()
    for i in range (0, len(lista)):
        if count(text,lista[i])>=max:
            if count(text,lista[i])>max:
                max=count(text,lista[i])
                mostfrq.clear()
                mostfrq.add(lista[i])
            else:
                mostfrq.add(lista[i])
    return mostfrq


def count(text, word):
    n=0
    for i in range (0, len(text)-len(word)+1):
        if kmer(text, i, len(word))==word:
                n=n+1
    return n

