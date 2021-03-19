#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

def pay(production, rate, bonus):
    return int(production) * int(rate) + int(bonus)


script_name, first_param, second_param, third_param = argv
print("Имя скрипта: ", script_name)
print("Выработка в часах: ", first_param)
print("Ставка в часах: ", second_param)
print("Премия: ", third_param)

print("Заработная плата сотрудника = ", pay(first_param, second_param, third_param))