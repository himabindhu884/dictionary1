d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d={}
for i in d1:
	for j in d2:
		if i in d2:
			d[i]=d2[i]+d1[i]
		elif j not in d1:
			d[j]=d2[j]
		elif i not in d2:
			d[i]=d1[i]
print(d)