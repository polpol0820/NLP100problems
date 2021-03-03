s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(",","").replace(".","")
l = list(s.split(" "))
num_li = []
for i in l:
    num_li.append(len(i))
print(num_li)