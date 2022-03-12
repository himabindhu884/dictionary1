d={1:50,2:70,3:20,4:5,5:0}
a=list(d.values())
max=0
i=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i+=1
min=a[0]
for i in a:
    if i<min:
        min=i
print("max",max)
print("min",min)
