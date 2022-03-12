d=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color':
'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
a=input("enter")
for i in range(len(a)):
    if d[i]['id']==a:
        del d[i]
        break
    elif d[i]['color']==a:
        del d[i]
        break
print(d)