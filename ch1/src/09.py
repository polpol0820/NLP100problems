import random
s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(s):
    s = s.split()
    ans = []
    for word in s:
        q = ""
        if len(word) >4:
            d = word[1:-1]
            d = random.sample(d,len(d))
            q = word[0]
            for i in range(len(d)):
                q += d[i]
            q+= word[-1]
            ans.append(q)
        else:
            ans.append(word)
    return ans
ans = typoglycemia(s)
print(*ans)