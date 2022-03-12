d='w3resource'
b=list(d)
c={ }
for i in d:
	if i in c:
		c[i]+=1
	else:
		c[i]=1
print(c)