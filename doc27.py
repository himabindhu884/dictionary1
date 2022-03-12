student = [{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False, 'name': 'Rabi'},{'id': 3, 'success': True, 'name': 'Alex'}]
sum=0
for i in range(len(student)):
    for j in (student[i]):
        if "id"==j:
            sum+=student[i][j]
print(sum)