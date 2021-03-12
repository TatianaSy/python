def my_func(x, y):
    result = 1
    for i in range(-y):
        result = result * (1 / x)
    return result


x=input("Введите действительное положительное число x: ")
try:
    x = float(x)
except ValueError as err:
    print("error!")
    print(err)

y=input("Введите целое отрицательное число y: ")
try:
    y = int(y)
    int(y)<0
except ValueError as err:
    print("error!")
    print(err)

print("x в степени -y = ", my_func(x, y))
