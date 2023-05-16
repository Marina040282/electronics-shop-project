from electronics_shop_project.src.item import Item


class Phone(Item):

    def __init__(self,name: str, price: float, quantity: int, number_of_sim: int):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный код
        self.number_of_sim = number_of_sim


    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __str__(self):
        return f"{self.name}"


    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def __radd__(self, other):
        if not isinstance(other, Item):
            return 'Складывать можно только объекты Item и дочерние от них.'
        else:
            return self.quantity + other.quantity
