d={'a':10,'b':20,'c':35,'d':70,'e':78}
a=list(d.values())
i=0
max=0
while i<len(d):
    if a[i]>max:
        max=a[i]
    i+=1
j=0
max1=0
while j<len(d):
    if a[j]<max:
        if a[j]>max1:
            max1=a[j]
    j+=1
k=0
max2=0
while k<len(d):
    if a[k]<max1:
        if a[k]>max2:
            max2=a[k]
    k+=1
print(max)
print(max1)
print(max2)