import json

res = dict()
aver_profit = 0  # начальное значение средней прибыли
num = 0  # начальное значение количества прибыльных предприятий
with open("text_7.txt", 'r', encoding="utf-8") as f:
    for line in f:  # 1я итерация цикла:
        name, type, income, cost = line.split()
        # на первой итерации получаем список - ['Brooms', 'ПАО', '2500000', '500000']
        # print(line.split())

        profit = int(income) - int(cost)  # 2500000 - 500000 = 2000000
        if profit >= 0:
            aver_profit += profit  # накапливаем значение прибыли
            num += 1  # увеличиваем значение количества прибыльных предприятий

        # добавляем элементы в словарь res = {'Brooms': 2000000}
        res[name] = profit
        # print(res)
aver_profit /= num  # средняя прибыль прибыльных предприятий
print(res)
# {'Brooms': 2000000, 'Tandoor': -635000, 'Honey-cake': 4795000, 'Matrioshka': 4259000, 'Сказка': 5500000}
with open("json7.json", "w", encoding="utf-8") as f:  # запись в файл
    json.dump([res, {"average_profit": aver_profit}],
              f, ensure_ascii=False)  # для кириллицы


with open("json7.json", "r", encoding="utf-8") as f:  # в обратную сторону из файла читаем

    res2 = json.load(f)

print(res2)