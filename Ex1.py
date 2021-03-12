def my_division(a, b):
    if b!=0:
        sub = a/b
        print ("a/b= ", sub)
    else:
        print("Ошибка: деление на 0!")


print("Чему равно a/b?")
my_division(int(input("a= ")), int(input("b= ")))