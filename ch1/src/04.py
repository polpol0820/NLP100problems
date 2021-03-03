s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace(",","").replace(".","")
l = s.split()
query = [1,5,6,7,8,9,15,16,19]
ans = {}
for key,val in enumerate(l):
    if key+1 in query:
        ans[val[:1]] = key+1
    else:
        ans[val[:2]] = key+1
print(ans)