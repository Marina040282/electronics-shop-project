import csv

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

        # Геттер для fullname
    @property
    def name_(self):
        """Возвращает имя сотрудника. К атрибуту можно обращаться без ()."""
        return f'{self.name}'

    @name_.setter
    def name_(self, name):
        """Метод срабатывает при операции присваивания."""
        if len(name) < 10:
            self.name = name


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


    def instantiate_from_csv(self):
        with open('C:/Users/Марина/PycharmProjects/pythonProject_4_OPP/electronics_shop_project/src/items.csv', 'r') as r_file:
            my_file = csv.reader(r_file, delimiter=",")
            line_number = 0
            for line in my_file:
                line_number += 1
                if line_number != 1:
                    self.name, self.price, self.quantity = line
                    self.all.append(line)
        return self.all

    def string_to_number(self, number) -> int:
        return int(float(number))

