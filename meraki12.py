i=0
square=0
while i<=15:
    square=i*i
    print(i,":",square,",",end="")
    i+=1



d={}
for i in range(1,16):
    d[i]=i**2
print(d)