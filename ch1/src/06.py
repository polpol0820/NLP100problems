s1 = "paraparaparadise"
s2 = "paragraph"

def ngram(n,l):
    ans = list(zip(*[l[i:] for i in range(n)])) 
    return ans

x = set(ngram(2,s1))
y = set(ngram(2,s2))
print("X：",x)
print("Y：",y)
print("和集合：",x|y)
print("積集合：",x&y)
print("差集合：",x-y)
print("Xにseが含まれるか：",{('s','e')} <= x)
print("Yにseが含まれるか：",{('s','e')} <= y)