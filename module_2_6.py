age = int(input(' Введите число от 3 до 20 :'))
result =[]
for i in range(1,21):
    if i == age:
        break
    for j in range(1,21):
        if i > j or i + j == 2 or i == j:
            continue
        if  age == i + j or age % (i + j) == 0:
           result.append(i)
           result.append(j)
print(*result)
