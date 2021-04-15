#Создайте собственный класс - исключение, обрабатывающий ситуацию деления на 0. Проверьте его работу на данных, вводимых
#пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
#завершиться с ошибкой.

class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


print(DivisionByZero.divide_by_zero(float(input("Введите делимое a= ")), float(input("Введите делитель b= "))))
print(DivisionByZero.divide_by_zero(float(input("Введите делимое a= ")), float(input("Введите делитель b= "))))
