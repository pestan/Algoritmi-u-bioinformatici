def kmer(text, i, k):
    return text[i: i+k]

    
def patterncount(text, pattern):
    count=0
    for i in range (0, len(text) - len(pattern) + 1):
        if kmer(text, i, len(pattern)) == pattern:
                count=count +1
    return count
