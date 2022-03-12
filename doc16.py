a={'name','class','age'}
b={'hima','mba',20}
d={}
for i in a:
    for j in b:
        d[i]=j
        b.remove(j)
        break
print(d)