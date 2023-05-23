import csv
import os
from csv import DictReader

path = r'C:/Users/Марина/PycharmProjects/pythonProject_4_OPP/electronics_shop_project/src/items.csv'

class InstantiateCSVError(Exception):
    """
    Класс для обработки собственных исключений
    """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity


    @property
    def name(self):
        """Возвращает имя сотрудника. К атрибуту можно обращаться без ()."""
        return f'{self.__name}'


    @name.setter
    def name(self, name_):
        """Метод срабатывает при операции присваивания."""
        if len(name_) < 10:
            self.__name = name_
        else:
            raise Exception('Длина наименования товара превышает 10 символов')


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open(path, 'r') as r_file:
                my_file = DictReader(r_file)
                if len(my_file.fieldnames) < 3:
                    raise InstantiateCSVError
                line_number = 0
                for line in my_file:
                    line_number += 1
                    if line_number != 1:
                        cls.name, cls.price, cls.quantity = line
                        cls.all.append(line)
            return cls.all
        except FileNotFoundError as e:
            print(f'Отсутствует файл item.csv')

    @staticmethod
    def string_to_number( number) -> int:
        return int(float(number))


    # Домашнее задание 14.1
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'



