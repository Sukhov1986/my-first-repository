# try:
#     number = int(input("Введите число -> "))
# except ValueError:
#     print("Должно быть число ")
#     exit()
# tpl = tuple(str(i) for i in str(number))
# print(tpl)
# lst = []
# for i in tpl:
#     if i not in lst:
#         lst.append(i)
# print(lst)
# for i in lst:
#     print(f"{i} = {tpl.count(i)}")

# string = input('Введите строку -> ').lower()
# vowels_1 = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
# vowels_2 = [x for x in string if x in vowels_1]
# print(f'Количество гласных равно : {len(vowels_2)}')

# dictionary_1 = {"name": "kelly", "age": 25, "salary": 8000, "city": "New York"}
# print(dictionary_1)
# dictionary_2 = {key: dictionary_1[key] for key in dictionary_1 if key in ["name", "salary"]}
# for i in dictionary_2:
#     dictionary_1.pop(i)
#
#
# print(dictionary_1)
# print(dictionary_2)
#

# # print(dictionary_1)
# dictionary_2 = {key: dictionary_1[key] for key in dictionary_1 if key in ["name", "salary"]}
# for i in dictionary_2:
#     dictionary_1.pop(i)
#
#
# print(dictionary_1)
# print(dictionary_2)


# from prettytable import PrettyTable
#
# Total_Sales = {'January': 52000, 'February': 51000, "March": 48000}
# Production_Cost = {'January': 46800, 'February': 45900, "March": 43200}
# profit = dict(zip(Total_Sales.keys(),
#                   [sales - cost for sales, cost in zip(list(Total_Sales.values()), list(Production_Cost.values()))]))

# # print(profit)

# print(profit)

# table = PrettyTable(['Element/Month', 'January', 'February', "March"])
# table.align = 'r'
# table.align['Element/Month'] = "l"
# table.add_row(['Total Sales', Total_Sales['January'], Total_Sales['February'], Total_Sales["March"]])
# table.add_row(['Production Cost', Production_Cost['January'], Production_Cost['February'], Production_Cost["March"]])
# table.add_row(['Profit', profit['January'], profit['February'], profit["March"]])
# print(table)


# def main():
#     quantity = int(input("Введите количество учеников :"))
#     return quantity
#
#
# def data(**kwargs):
#     return kwargs
#
#
# def data_input():
#     s_surname = input("Введите фамилию :")
#     s_name = input("Введите имя :")
#     s_point = int(input("Введите балл :"))
#     return s_surname, s_name, s_point
#
#
# students = main()
# lst = []
# res = 0
# for i in range(students):
#     a, b, c = data_input()
#     res += c
#     x = data(surname=a, name=b, point=c)
#     lst.append(x)
# average_mark = res / students
# average_result = round(average_mark)
# print(f"Средний балл {average_result}. Студенты с баллом выше среднего :")
# for i in lst:
#     if i["point"] > average_result:
#         print(i["name"])

from math import pi

figures = {
    "circle": lambda x: x ** 2 * pi,
    "rectangle": lambda x, y: x * y,
    "trapezoid": lambda a, b, h: 0.5 * (a + b) * h
}


def circle():
    x = int(input("Введите радиус : "))
    return x


def rectangle():
    x, y = [int(input(f"Введите сторону прямоугольника {i} : ")) for i in ["1", "2"]]
    return x, y


def trapezoid():
    x, y, z = [int(input(f"Введите {i} : ")) for i in ["длину основания 1", "длину основания 2", "высоту"]]
    return x, y, z


circle_ = circle()
side_1, side_2 = rectangle()
base_1, base_2, height = trapezoid()

print(f"Площадь окружности радиуса {circle_} : {figures['circle'](circle_)}")
print(f"Площадь прямоугольника размером {side_1}*{side_2} : {figures['rectangle'](side_1, side_2)}")
print(f"Площадь трапеции для a={base_1}, b={base_2}, h={height} : {figures['trapezoid'](base_1, base_2, height)}")


def decorator(fn):
    def wrapper(*args):
        return fn(*args) / len(args)

    return wrapper


@decorator
def summ(*args):
    return sum(args)


print(summ(2, 3, 3, 4))


def function(x, y):
    if x > y:
        x, y = y, x
    return list(map(chr, [i for i in range(x, y + 1)]))


a, b = 122, 97

print(*function(a, b))

str1 = "I am learning Python. hello, WORLD!"
letter = "h"
str1 = str1[:str1.find(letter) + 1] + str1[str1.find(letter) + 1:str1.rfind(letter)][::-1] + str1[str1.rfind(letter):]
print(str1)

import re

text_ = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
pattern = r"[\w.-]+@[\w.]*\.ru\b"
print(re.findall(pattern, text_))

import re

tel = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78 "
req = r"\+*7(?:[\s(]*\d{3}[\s)]*){2}[-\s]*\d{2}[\s-]*\d{2}"
print(re.findall(req, tel))


def negative_number(n):
    if not n:
        return 0
    count = 0
    if n[0] < 0:
        count += 1
    return count + negative_number(n[1:])


lst = [-2, 3, 8, -11, -4, 6]
print(negative_number(lst))

txt = ("Замена строки в текстовом файле;\n"
       "Записать список в файл;\n"
       "Изменить строку в списке;\n")


def file_creation(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)


def replacement(file):
    with open(file, "r") as f:
        lines = f.readlines()
    while True:
        pos1, pos2 = [int(input(f"Заменить {val}")) for val in ["строку: ", "на строку: "]]
        if 0 < pos1 <= len(lines) and 0 < pos2 <= len(lines):
            lines[pos1 - 1], lines[pos2 - 1] = lines[pos2 - 1], lines[pos1 - 1]
            break
        else:
            print(f"Неверный диапазон строк.Допустимое значение от 1 до {len(lines)}")

    with open(file, "w") as f:
        f.writelines(lines)


file_creation("filename.txt", txt)
replacement("filename.txt")

import os

dirs = "Homework"
nested = ["test", "test1"]
file_name = ["project.txt", "test.txt"]
for d in nested:
    os.makedirs(os.path.join(dirs, d), exist_ok=True)
    for file in file_name:
        file_path = os.path.join(dirs, file)
        with open(file_path, "w") as f:
            f.write(f"Это файл {file}")


def scanning(directory):
    if os.path.exists(directory):
        contents = os.listdir(directory)
        for i in contents:
            full_path = os.path.join(directory, i)
            print(f"{i} - file - {os.path.getsize(full_path)} bytes" if os.path.isfile(full_path) else f"{i} - dir")
    else:
        print("Такого пути не существует")


scanning(dirs)


class Automobile:
    def __init__(self):
        self.model = ""
        self.year = ""
        self.manufacturer = ""
        self.engine_power = ""
        self.color = ""
        self.price = ""

    def input_data(self):
        self.model = input("Модель автомобиля :")
        self.year = input("Год выпуска :")
        self.manufacturer = input("Производитель :")
        self.engine_power = input("Мощность двигателя :")
        self.color = input("Цвет машины :")
        self.price = input("Цена :")

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель : {self.manufacturer}")
        print(f"Мощность двигателя : {self.engine_power} л.с.")
        print(f"Цвет машины : {self.color}")
        print(f"Цена : {self.price}")
        print("=" * 40)

    def update_model(self):
        new_model = input("Введите новую модель автомобиля: ")
        self.model = new_model

    def update_year(self):
        new_year = input("Введите новый год выпуска: ")
        self.year = new_year

    def update_manufacturer(self):
        new_manufacturer = input("Введите нового производителя: ")
        self.manufacturer = new_manufacturer

    def update_engine_power(self):
        new_engine_power = input("Введите новую мощность двигателя: ")
        self.engine_power = new_engine_power

    def update_color(self):
        new_color = input("Введите новый цвет машины: ")
        self.color = new_color

    def update_price(self):
        new_price = input("Введите новую цену: ")
        self.price = new_price


car1 = Automobile()
car1.input_data()
car1.print_info()
car1.update_color()
car1.print_info()

import turtle  # нужно импортировать модуль


class Rectangle:
    def __init__(self):
        self.length = int(input("Введите длину прямоугольника : "))
        self.width = int(input("Введите ширину прямоугольника : "))

    def methods(self):
        while True:
            print("Выберите интересующий вас метод: ".center(40, "*"))
            print("1 Площадь прямоугольника\n"
                  "2 Периметр прямоугольника\n"
                  "3 Гипотенуза прямоугольника\n"
                  "4 Нарисовать прямоугольник")
            choice = int(input("Введите номер метода : "))
            if choice == 1:
                self.square()
            elif choice == 2:
                self.perimeter()
            elif choice == 3:
                self.hypotenuse()
            elif choice == 4:
                self.draw()
            else:
                print("Введите правильный номер метода".center(40, "*"))
            if 0 < choice < 5:
                break

    def square(self):
        print(f"Площадь прямоугольника: {self.length * self.width}")

    def perimeter(self):
        print(f"Периметр прямоугольника: {2 * (self.length + self.width)}")

    def hypotenuse(self):
        print(f"Гипотенуза прямоугольника: {0.5 * (self.length ** 2 + self.width ** 2)}")

    def draw(self):
        t = turtle.Turtle()
        for _ in range(2):
            t.forward(self.length)
            t.left(90)
            t.forward(self.width)
            t.left(90)
        turtle.done()


rectangle1 = Rectangle()
rectangle1.methods()


class Person:

    def __init__(self, name, old):
        if Person.__check_value_old(old) and Person.__check_value_name(name):
            self.__name = name
            self.__old = old
        else:
            raise ValueError("Неправильный ввод данных")

    @staticmethod
    def __check_value_name(n):
        if isinstance(n, str):
            return True
        return False

    @staticmethod
    def __check_value_old(o):
        if isinstance(o, int):
            return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if Person.__check_value_name(new_name):
            self.__name = new_name
        else:
            print("Имя должно быть строкой")

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        if Person.__check_value_old(new_old):
            self.__old = new_old
        else:
            print("Возраст должен быть числом")

    @old.deleter
    def old(self):
        del self.__old


person1 = Person("Irina", 26)
print(person1.name)
print(person1.old)
person1.name = "Igor"
person1.old = 31
print(person1.name)
print(person1.old)
del person1.name
print(person1.__dict__)

import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value

        print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    @staticmethod
    def __check_surname(surname):
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть строкой")
        if not re.match("^[a-zа-яё-]+$", surname, re.IGNORECASE):
            raise ValueError("Фамилия должна состоять только из букв")

    @staticmethod
    def __check_num(num):
        if not isinstance(num, str):
            raise TypeError("Счет должен передаваться строкой")
        if not num.isdigit():
            raise TypeError("Счет должен состоять из цифр")

    @staticmethod
    def __check_percent(percent):
        if not isinstance(percent, float):
            raise TypeError("Процент должен быть вещественным числом")
        if percent < 0:
            raise ValueError("Процент не может быть отрицательным числом")

    @staticmethod
    def __check_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Баланс долен быть числом")
        if value < 0:
            raise ValueError("Баланс должен быть положительным числом")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, s):
        self.__check_surname(s)
        self.__surname = s

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, n):
        self.__check_num(n)
        self.__num = n

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, p):
        self.__check_percent(p)
        self.__percent = p

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, v):
        self.__check_value(v)
        self.__value = v

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        uer_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счёта: {uer_val} {Account.suffix_eur}")

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снять!")
        self.print_balance()

    def print_info(self):
        print('Информация о счете:')
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


acc = Account("Долгих", "12345", 0.03, 1000)
acc.surname = "Иванов"
print(acc.surname)
acc.num = "987654321"
print(acc.num)
acc.percent = 0.05
print(acc.percent)
acc.value = 10000
print(acc.value)

acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
print()
acc.convert_to_usd()
acc.convert_to_eur()
acc.edit_owner("Дюма")
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(3000)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)

import re


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        self.set_surname(surname)
        self.set_num(num)
        self.set_percent(percent)
        self.set_value(value)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def get_surname(self):
        return self.__surname

    def set_surname(self, s):
        self.__check_surname(s)
        self.__surname = s

    def get_num(self):
        return self.__num

    def set_num(self, n):
        self.__check_num(n)
        self.__num = n

    def get_percent(self):
        return self.__percent

    def set_percent(self, p):
        self.__check_percent(p)
        self.__percent = p

    def get_value(self):
        return self.__value

    def set_value(self, v):
        self.__check_value(v)
        self.__value = v

    @staticmethod
    def __check_surname(surname):
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть строкой")
        if not re.match("^[a-zа-яё-]+$", surname, re.IGNORECASE):
            raise ValueError("Фамилия должна состоять только из букв")

    @staticmethod
    def __check_num(num):
        if not isinstance(num, str):
            raise TypeError("Счет должен передаваться строкой")
        if not num.isdigit():
            raise TypeError("Счет должен состоять из цифр")

    @staticmethod
    def __check_percent(percent):
        if not isinstance(percent, float):
            raise TypeError("Процент должен быть вещественным числом")
        if percent < 0:
            raise ValueError("Процент не может быть отрицательным числом")

    @staticmethod
    def __check_value(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Баланс долен быть числом")
        if value < 0:
            raise ValueError("Баланс должен быть положительным числом")

    def add_money(self, val):
        self.__value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        uer_val = Account.convert(self.__value, Account.rate_eur)
        print(f"Состояние счёта: {uer_val} {Account.suffix_eur}")

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percent(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.__value -= val
            print(f"{val} {Account.suffix} было успешно снять!")
        self.print_balance()

    def print_info(self):
        print('Информация о счете:')
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)


acc = Account("Долгих", "12345", 0.03, 1000)
acc.set_surname("Иванов")
print(acc.get_surname())
acc.set_num("987654321")
print(acc.get_num())
acc.set_percent(0.05)
print(acc.get_percent())
acc.set_value(10000)
print(acc.get_value())

acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
print()
acc.convert_to_usd()
acc.convert_to_eur()
acc.edit_owner("Дюма")
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(3000)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)

import math


class Table:
    def __init__(self, *args):
        if len(args) == 2:
            self._width = args[0]
            self._height = args[1]
        elif len(args) == 1:
            self._radius = args[0]


class Rectangular(Table):

    def square(self):
        return self._width * self._height


class Round(Table):
    def square(self):
        return round(math.pi * self._radius ** 2, 2)


rectangular_table = Rectangular(20, 20)
print(rectangular_table.square())
round_table = Round(20)
print(round_table.square())


class Student:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"{self.name} => {Student.Information.model}, {Student.Information.cpu}, {Student.Information.memory}")

    class Information:
        model = "HP"
        cpu = "i7"
        memory = 16


winner_1 = Student("Roman")
winner_1.print_info()
winner_2 = Student("Vladimir")
winner_2.print_info()

from copy import deepcopy


class Clock:
    DAY = 86400

    def __init__(self, sec, name=None):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.DAY
        self.name = name

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __str__(self):
        return self.get_format_time()

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ValueError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ValueError("Правый операнд должен быть типом Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ValueError("Правый операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ValueError("Правый операнд должен быть типом Clock")
        return Clock(self.sec // other.sec)


c1 = Clock(600, "c1")
c2 = Clock(200, "c2")
print(f"{c1.name}: {c1.get_format_time()}")
print(f"{c2.name}: {c2.get_format_time()}")
print(f"{c1.name} + {c2.name}: {c1 + c2}")
print(f"{c1.name} - {c2.name}: {c1 - c2}")
print(f"{c1.name} * {c2.name}: {c1 * c2}")
print(f"{c1.name} // {c2.name}: {c1 // c2}")
c1_copy = deepcopy(c1)
c1_copy += c2
print(f"c1 += c2: {c1_copy}")
c1_copy -= c2
print(f"c1 -= c2: {c1_copy}")
c1_copy *= c2
print(f"c1 *= c2: {c1_copy}")
c1_copy //= c2
print(f"c1 //= c2: {c1_copy}")


class Point3D:
    def __init__(self, x, y, z):
        self.data = {"x": x, "y": y, "z": z}

    def __str__(self):
        return f"({self.data['x']}, {self.data['y']}, {self.data['z']})"

    def __add__(self, other):
        return Point3D(self.data['x'] + other.data['x'], self.data['y'] + other.data['y'],
                       self.data['z'] + other.data['z'])

    def __sub__(self, other):
        return Point3D(self.data['x'] - other.data['x'], self.data['y'] - other.data['y'],
                       self.data['z'] - other.data['z'])

    def __mul__(self, other):
        return Point3D(self.data['x'] * other.data['x'], self.data['y'] * other.data['y'],
                       self.data['z'] * other.data['z'])

    def __truediv__(self, other):
        return Point3D(self.data['x'] / other.data['x'], self.data['y'] / other.data['y'],
                       self.data['z'] / other.data['z'])

    def __eq__(self, other):
        return (self.data['x'] == other.data['x'] and self.data['y'] == other.data['y'] and
                self.data['z'] == other.data['z'])

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError("Неправильный тип данных ключа")
        if item in self.data:
            return self.data[item]
        else:
            raise KeyError("Неверный ключ")

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Неправильный тип данных ключа")
        if not isinstance(value, int):
            raise TypeError("Неправильный тип данных значения")
        if key in self.data:
            self.data[key] = value
        else:
            raise KeyError("Неверный ключ")


point1 = Point3D(12, 15, 18)
point2 = Point3D(6, 3, 9)
print(f"Сложение координат:  {point1 + point2}")
print(f"Вычитание координат:  {point1 - point2}")
print(f"Умножение:  {point1 * point2}")
print(f"Деление:  {point1 / point2}")
print(f"Равенство координат: {point1 == point2}")
print(f"Получение координаты {point1['x']}")
point1["x"] = 20
print(f"Запись значения в координату x: {point1['x']}")


class Descriptor:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.__name} должно быть числом")
        if value < 0:
            raise ValueError(f"{self.__name} должно быть положительным числом")
        instance.__dict__[self.__name] = value


class Order:
    price = Descriptor()
    quantity = Descriptor()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def summ(self):
        return self.price * self.quantity


purchase1 = Order('apple', 5, 10)
print(purchase1.summ())

import json
from random import choice


def gen_person():
    name = ""
    tel = ""
    keys = ""

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letter)

    while len(tel) != 10:
        tel += choice(num)

    while len(keys) != 10:
        keys += choice(num)

    person = {
        keys:
            {'name': name,
             'tel': tel}
    }
    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())

import json


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Студент: {self.name}: {', '.join(map(str, self.marks))}"

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def dump_to_json(self):
        data = {"name": self.name, "marks": self.marks}
        with open(self.get_file_name(), "w") as f:
            json.dump(data, f)

    def load_from_file(self):
        with open(self.get_file_name(), "r") as f:
            print(json.load(f))

    def get_file_name(self):
        return self.name + ".json"


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    @staticmethod
    def change_group(group_1, group_2, index):
        tmp = group_1.remove_student(index)
        group_2.add_student(tmp)

    @staticmethod
    def write_groups_json(self):
        try:
            data = json.load(open('groups.json'))
        except FileNotFoundError:
            data = {}

        group_data = {
            self.group: {
                student.name: student.marks for student in self.students
            }
        }
        data.update(group_data)

        with open('groups.json', 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load_groups_file():
        with open('groups.json', "r") as f:
            return json.load(f)

    def __str__(self):
        a = '\n'.join(map(str, self.students))
        return f"\nГруппа: {self.group}\n{a}"

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    def dump_to_json(self):
        data = [
            {"name": student.name, "marks": student.marks} for student in self.students
        ]

        with open(self.get_file_name(), "w") as f:
            json.dump(data, f)

    def get_file_name(self):
        return self.group.lower().replace(" ", "-") + ".json"

    def load_from_file(self):
        with open(self.get_file_name(), "r") as f:
            return json.load(f)


st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
sts1 = [st1, st2]
group1 = Group(sts1, "ГК Python")
print(group1)
group1.add_student(st3)
group1.remove_student(1)
print(group1)
sts2 = [st2]
group2 = Group(sts2, "ГК Web")
# print(group2)
Group.change_group(group1, group2, 0)
# print(group1)
# print(group2)
group1.dump_to_json()
group2.dump_to_json()
print(group1.load_from_file())
print(group2.load_from_file())
print(st1)
st1.add_mark(4)
# print(st1)
st1.delete_mark(2)
# print(st1)
st1.edit_mark(4, 5)
# print(st1)
# print(st1.average_mark())
st1.dump_to_json()
st1.load_from_file()
Group.write_groups_json(group1)
Group.write_groups_json(group2)
print("*" * 100)
print(Group.load_groups_file())

import pandas as pd

data = pd.read_csv('data2.csv')
print(data)

import sqlite3

with sqlite3.connect('mydatabase.db') as conn:
    cursor = conn.cursor()
    sql_lst = [
        """CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        surname TEXT,
        name TEXT,
        patronymic TEXT,
        age INTEGER,
        "group" TEXT,
        FOREIGN KEY("group") REFERENCES groups(id));
        """,
        """CREATE TABLE IF NOT EXISTS groups(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT
    );""",
        """CREATE TABLE IF NOT EXISTS association(
        lesson_id INTEGER,
        group_id INTEGER,
        FOREIGN KEY(group_id) REFERENCES groups(id),
        FOREIGN KEY(lesson_id) REFERENCES lessons(id)
    );""",
        """CREATE TABLE IF NOT EXISTS lessons(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lessons_title TEXT
    );"""
    ]
    for i in sql_lst:
        cursor.execute(i)
