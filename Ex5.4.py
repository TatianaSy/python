f1 = open('primer4.txt', 'r', encoding="utf-8")
content = f1.readline()
new_list = []

while content != '':
    string = content.split(' ')
        new_list.append(string)  # добавляем в список
    content = f1.readline()  # считали очередную  строку из файла
f1.close()

for i in range(len(new_list)):
    if i == 0:
        new_list[i][0] = "Один"
    elif i == 1:
        new_list[i][0] = "Два"
    elif i == 2:
        new_list[i][0] = "Три"
    else:
        new_list[i][0] = "Четыре"

f1 = open('primer4n.txt', 'w', encoding="utf-8")  # создаем новый файл
f1.close()
f1 = open('primer4n.txt', 'a', encoding="utf-8")
for i in range(len(new_list)):
    s = ",".join(new_list[i])
    # print(s.replace(',', ' '), end='')
    # очередную строку пишем в файл
    print(s.replace(',', ' '), end='', file=f1)

f1.close()