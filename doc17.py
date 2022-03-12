d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
a=sorted(d.items())
b={}
for i in a:
    b.update({i[0]:i[1]})
print(b)