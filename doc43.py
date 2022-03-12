a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
b={}
c=[ ]
d=[ ]
e=[ ]
for i,j in a:
    if i=="yellow":
        c.append(j)
        b[i]=c
    elif i=="blue":
        d.append(j)
        b[i]=d
    elif i=="red":
        e.append(j)
        b[i]=e
print(b)