n = ['10+10+10']
p = []
z = 0
for i in n:
    if "+" in i:
        x = i.split("+")
        for i in x:
            z += int(i)
        p.append(z)
        z = 0
    else:
        p.append(int(i))
k = p[0]
for i in range(1, len(p)):
    k -= p[i]
print(k)