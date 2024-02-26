def create_pass(s):
    """ Функция генерации пароля, где <s> - список данных по одному кораблю """
    n = ""
    n += s[1][-3:]
    n += s[0].split("-")[0][1:3][::-1]
    n += s[1][:3][::-1]
    return n.upper()


f = open("space.txt").read()
f = f.split("\n")
header = f.pop(0)
data = [i.split("*") for i in f]

''' сверху подготовка данных для работы '''

''' снизу перезапись данных вместе с паролем '''

ans = open("space_uniq_password.csv", "w")
ans.write(";".join(header.split("*")) + ";" + "password")
for i in data:
    pas = create_pass(i)
    ans.write("\n")
    ans.write(";".join(i) + ";" + f'{pas}')
ans.close()
