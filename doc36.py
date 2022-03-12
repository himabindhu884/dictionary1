a={'key1': 1, 'key2': 3, 'key3': 2}
b={'key1': 1, 'key2': 2}
for i in a:
    for j in b:
        w=a[i]
        x=b[j]
        if i==j and w==x:
            print(i,':',w,'is present in both a and b')