f1 = open('primer3.txt', 'r', encoding="utf-8")
content = f1.readline()

new_list = []
wages = 0
while content != '':

    string = content.split()

    new_list.append(string)  # добавляем в список
    content = f1.readline()  # считали очередную  строку из файла
f1.close()

for i in range(len(new_list)):
    wages = wages + float(new_list[i][1])  # суммируем зар. плату
    if float(new_list[i][1]) < 20000:
        print(new_list[i][0])  # сотрудники с з. платой меньше 20000 р.
average = wages / len(new_list)  # средняя  зар. плата
print(average)