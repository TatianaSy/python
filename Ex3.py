def my_func(a1, a2, a3):
    my_list = [a1, a2, a3]
    my_list.remove(min(a1, a2, a3))
    return sum(my_list)


print(my_func(1, 9, 4))
print(my_func(1, -2, -4))