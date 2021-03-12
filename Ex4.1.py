def my_func(x, y):
    return x ** y

x=input("Введите действительное положительное число x: ")
try:
    x = float(x)
except ValueError as err:
    print("error!")
    print(err)

y=int(input("Введите целое отрицательное число y: "))
try:
    int(y)<0
except ValueError as err:
    print("error!")
    print(err)

print("x в степени -y = ", my_func(x, y))

