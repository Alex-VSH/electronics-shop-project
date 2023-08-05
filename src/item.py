import csv
import os


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
        self.quantity = quantity
        self.price = price
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        operation_path = os.path.join(os.path.dirname(__file__), "items.csv")
        with open(operation_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            reader = list(reader)
            for i in range(1, len(reader)):
                new_item = Item(reader[i][0], float(reader[i][1]), int(reader[i][2]))
                Item.all.append(new_item)


    @staticmethod
    def string_to_number(number):
        return int(float(number))


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:       # Тут можно сделать короче, но задание просит именно проверку на длинну
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
