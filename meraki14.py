d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("original order:",d)
dic=sorted(d.items())
print("asc order:",dic)
dic1=sorted(d.items(),reverse=True)
print('dsc order:',dic1)