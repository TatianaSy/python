#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
my_list = input("Введите числа через пробел: ").split()
print(my_list)
new_list = [my_list[i+1] for i in range(len(my_list)-1) if my_list[i+1] > my_list[i]]
print(new_list)