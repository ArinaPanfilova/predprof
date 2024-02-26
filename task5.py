f = open("space.txt").read()
f = f.split("\n")
header = f.pop(0)
data = [i.split("*") for i in f]

''' сверху подготовка данных для работы '''

'''снизу создание хэш-таблицы("hash_table") в формате словаря '''
hash_table = {}
data.sort(key=lambda x: x[1])
name = data[0][1]
korab = []
for i in data:
    if i[1] != name:
        hash_table[name] = korab
        name = i[1]
        korab = [i[0]]
    else:
        korab.append(i[0])
hash_table[name] = korab

''' снизу функция, которая будет выводить все корабли улетевшие с заданной планеты("planet") '''


def show_korabli(planet):
    for i in hash_table[planet]:
        print(f'{planet}: {i}')


''' вывод информации о 10 кораблях, с использованием написанной выше функции '''
show_korabli("Абеллио")
show_korabli("Аглатосия")
show_korabli("Арда")
show_korabli("Беренс")
show_korabli("Валинор")
show_korabli("Голевард")
