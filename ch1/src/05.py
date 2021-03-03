#n-gramとはn個の連続する単位

def ngram(n,l):
    ans = list(zip(*[l[i:] for i in range(n)])) 
    return ans

s = "I am an NLPer"

bigram_words = ngram(2,s.split())
bigram_chars = ngram(2,s)
print("単語bigram：",bigram_words)
print("文字bigram：",bigram_chars)
