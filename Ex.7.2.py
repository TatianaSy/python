#Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

class Textil:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def count_c(self):
        return self.size / 6.5 + 0.5


    def count_s(self):
        return self.height * 2 + 0.3

    @property
    def count_full(self):
        return str(f'Общий расход ткани на костюм и пальто \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.count_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Расход на 1 пальто - метров {self.count_c}'


class Suit(Textil):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.count_s = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход на 1 костюм - метров {self.count_s}'

coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)

#затруднения с расчетом общего расхода ткани. Да и приведенные в качестве примера формулы тоже, видимо, не поняла, от чего они зависят

