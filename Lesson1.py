#задача 1#
a = 5
b = a + 20
print("5+20=", b)
age = input("Введите ваш возраст: ")
print(age)
c="text"
print(c)

#задача 2#
t=int(input("Введите время в секундах: "))
m=t//60%60
print(m)
h=m//60%24
print(h)
t=60%60
print(f"{h:02d}:{m:02d}:{t:02d}")

#задача 3#
n=int(input("Введите целое число: "))
a=n
nn=n+n
nn=n+n+n
n=int(n)
nn=int(nn)
nnn=int(nnn)
print(n+nn+nnn)

#задача 4#
n=int(input("Введите целое положительное число: "))
max=0  # наибольшее число#
while n > 0:
    c = n % 5  #последняя цифра#
    n = n // 5  #число без последней цифры#
    if c > max:
        max = c
print(max)

#задача 5#
p=int(input("Выручка =  "))
c=int(input("Издержки = "))
r=p-c #результат#
print("результат: ", r)
if r > 0:
    print("Фирма работает с прибылью")
    rentab = r/p
    print('рентабельность = ', round(rentab, 2))  #округление
    s=int(input("Введите количество сотрудников: ")) #сотрудники
    print("Прибыль на одного сотрудника: ", round(p/s, 2))  #округление
else:
    print("Фирма работает с убытком")

#задача 6#
a = int(input())
b = int(input())
i = 0
while a < b:
    i = i + 1
    #print(i, "-й " + "день: ", round(a, 2), sep='')
    a = a * 1.1
print(i + 1)