n=0
try:
    while True:
        for i in map(int, input("Введите числа через пробел: ").split()):
            n += i
        print(n)
except ValueError:
    print(n)
