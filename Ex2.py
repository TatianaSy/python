def user_info(name, surname, year, city, email, telephone):
    print(name, surname, year, city, email, telephone)


user_info(name=input("Ваше имя: "), surname=input("Ваша фамилия: "), year=input("Год рождения: "),
              city=input("Город проживания: "), email=input("Адрес электронной почты: "), telephone=input("Номер телефона: "))