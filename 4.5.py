#Реализовать формирование списка, используя функцию range() и возможности генератора.
#В список должны войти четные числа от 100 до 1000 (включая границы).
from functools import reduce

def my_func (prev_el, el):
    return prev_el * el

new_list = [i for i in range(100,1001) if i % 2 == 0 ]

print(reduce(my_func, new_list))