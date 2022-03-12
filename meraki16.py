dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
i=0
while i<len(dic):
    j=0
    while j<len(dic):
        if dic[i]<dic[j]:
            dic[i],dic[j]=dic[j],dic[i]
        j+=1
    i+=1
print(dic)




d={"bijinder":45,"deepak":60,"param":20,"anjili":30,"roshini":50}
print(sorted(d.values()))


x=("key1","key2","key3")
y=1
dict=dict.fromkeys(x,y)
print(dict)
print(dict)