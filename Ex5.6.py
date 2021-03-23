d = dict()
with open("text_6.txt", 'r', encoding="utf-8") as f:
    for line in f:
        list1 = line.split(':')  # Fizra: - 30(пр) -   делим по : и получаем
        # ['Fizra', ' - 30(пр) -\n'] список из двух элементов
        print('list1 = ', list1)
        print('list1[0] = ', list1[0])  # Fizra  первый элемент списка
        print('list1[1] = ', list1[1])  # - 30(пр) -  второй элемент списка
        # - 30(пр) -    делим по пробелу второй элемент списка и получаем
        list2 = list1[1].split()
        # ['-', '30(пр)', '-'] список из трех элементов
        print('list2 = ', list2)

        num = 0
        for part in list2:  # комментарии для первой итерации цикла:
            if "-" in part:  # ['-', '30(пр)', '-']
                continue  # пропускаем, если элемент равен '-'
            list3 = part.split(
                '(')  # делим элемент '30(пр)' по скобке
            print(list3)  # ['30', 'пр)']
            print(list3[0])  # 30
            print(list3[1])  # пр)
            num += int(list3[0])  # суммируем числа

            d[list1[0]] = num
            print(d[list1[0]])  # 30
print(d)