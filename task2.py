f = open("space.txt").read()
f = f.split("\n")
header = f.pop(0)
data = [i.split("*") for i in f]

#  '''сверху подготовка необходимых данных'''

#  '''снизу сортировка выбором по заданному правилу'''
for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if int(data[j][0].split("-")[1]) < int(data[j - 1][0].split("-")[1]):
            data[j], data[j - 1] = data[j - 1], data[j]
        else:
            break

for i in range(10):
    print(data[i][0])
