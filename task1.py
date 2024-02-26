f = open("space.txt").read()
f = f.split("\n")
header = f.pop(0)
data = [i.split("*") for i in f]

''' сверху подготовка данных для работы '''

ans = open("space_new.txt", "w")
ans.write(header)
for i in data:
    ans.write("\n")

    ''' снизу создание координат по формуле '''

    if i[2].split()[0] == "0" and i[2].split()[0] == "0":
        pp = i[3].split()
        n = int(i[0][5])
        m = int(i[0][6])
        t = len(i[1])
        if n > 5:
            x = n + int(pp[0])
        else:
            x = -(n + int(pp[0])) * 4 + t
        if m > 3:
            y = m + t + int(pp[1])
        else:
            y = -(n + int(pp[1])) * m
        i[2] = f"{x} {y}"

    ''' снизу запись в файл новых данных '''
    ans.write("*".join(i))

    ''' вывод кораблей по данному правилу '''
    if i[0][3] == "V":
        print(f'{i[0]} - ({i[2].split()[0]}, {i[2].split()[1]})')
ans.close()
