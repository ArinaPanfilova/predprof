f = open("space.txt").read()
f = f.split("\n")
header = f.pop(0)
data = [i.split("*") for i in f]

#  '''сверху подготовка необходимых данных'''

while True:
    name = input()
    if name == "stop":
        break
    key = ""

    #  '''сверху подготовка к поиску и проверка на завершение'''

    #  '''снизу поиск и вывод найденной информации'''
    for i in data:
        if i[0] == name:
            key = i
            break
    if key:
        print(f'Корабль {key[0]} был отправлен с планеты: {key[1]} и его направление движения было: {key[-1]}')
    else:
        print("error.. er.. ror..")