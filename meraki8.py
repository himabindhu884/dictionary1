a=int(input("num"))
b={}
for i in range(a):
	c=input("keys")
	d=int(input("values"))
	b.update({c:d})
print(b)