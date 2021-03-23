import random
f1 = open('primer5.txt', 'w', encoding="utf-8")  # создаем новый файл
n = int(input())
for i in range(n):
    print(random.randint(1, 100), file=f1, end=' ')
f1.close()



# my_list = [i * 2 for i in range(n)] # использую генератор
#f1 = open('primer5.txt', 'w', encoding="utf-8")  # создаем новый файл
## print(my_list)
#for i in range(n):
    #print(my_list[i], file=f1, end=' ')
#f1.close()

f1 = open('primer5.txt', 'r', encoding="utf-8")
new_list = f1.read()


m_list = new_list.split()
summa = 0
for i in range(n):
    summa = summa + int(m_list[i])
print(summa)
f1.close()