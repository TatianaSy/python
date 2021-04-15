#Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class StoreDevices:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_dev = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


    def reception(self):

        try:
            dev = input(f'Введите наименование ')
            dev_p = int(input(f'Введите цену за ед '))
            dev_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_dev.update(unique)
            self.my_store.append(self.my_dev)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreDevices.reception(self)


class Printer(StoreDevices):
    def to_print(self):
        return f'to print devices {self.numb} times'


class Scanner(StoreDevices):
    def to_scan(self):
        return f'to scan devices {self.numb} times'


class Copier(StoreDevices):
    def to_copier(self):
        return f'to copier devices  {self.numb} times'


dev_1 = Printer('hp', 2000, 5, 10)
dev_2 = Scanner('Canon', 1200, 5, 10)
dev_3 = Copier('Xerox', 1500, 1, 15)
print(dev_1.reception())
print(dev_2.reception())
print(dev_3.reception())
print(dev_1.to_print())
print(dev_3.to_copier())