# задача №1
my_list = [6, -10, 35.7, 'stm', True, [-8, 2]]
for i in range(len(my_list)):
    print(type(my_list[i]))

# задача №2
my_list = input("Введите элементы списка: ").split()  # вводим список
print(my_list)
if len(my_list) % 2 == 0:  # четность количества элементов
    for i in range(0, len(my_list) - 1, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # обмен для четного количества элементов
else:
    for i in range(0, len(my_list) - 2, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # обмен для нечетного количества элементов
print(my_list)

# задача №3 (К какому времени года относится месяц)
print("К какому времени года относится месяц?")
season = [['1', 'Зима'], ['2', 'Зима'], ['3', 'Весна'], ['4', 'Весна'], ['5', 'Весна'], ['6', 'Лето'], ['7', 'Лето'], ['8', 'Лето'],
         ['9', 'Осень'], ['10', 'Осень'], ['11', 'Осень'], ['12', 'Зима'], ]
my_dict = dict(season)
print(my_dict[input("Введите номер месяца: ")])

# задача №4
words = input("Введите слова через пробел : ")
my_list = words.split()
# print(a)
for i in range(len(my_list)):
    if len(my_list[i]) <= 10:
        print(i + 1, 'слово', '-', my_list[i])
    else:
        print(i + 1, 'слово', '-', my_list[i][:10])


# задача №5
print("Рейтинг: 7, 5, 3, 3, 2.")
my_list = [7, 5, 3, 3, 2]  # исходный набор чисел
my_lst = "".join(map(str, my_list))  # вытащить элементы из списка 75332
new_el = input('Введите новый элемент рейтинга: ')

if new_el in my_lst:  # такой элемент уже существует в рейтинге
    index = my_lst.rfind(new_el)
    my_list.insert((index + 1), int(new_el))  # добавили повоторяющийся элемент
    print(my_list)
else:  # такого элемента еще нет в рейтинге
    my_list.append(int(new_el))  # добавили элемент в конец списка
    my_list.sort(reverse=True)  # сортируем список по убыванию
    print(my_list)


# задача №6
goods = [(1, {"компьютер", "цена = 20000 руб.", "количество = 5 шт."}), (2, {"принтер", "цена = 8000 руб.", "количество = 2 шт."}),\
        (3, {"сканер", "цена = 5000 руб.", "количество = 7 шт."})]
my_dict = dict(goods)
print(my_dict[input("Введите номер товара: ")])