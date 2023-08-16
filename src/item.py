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
        super().__init__()
        self.quantity = quantity
        self.price = price
        self.__name = name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Объект не класса Item или Phone')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @classmethod
    def instantiate_from_csv(cls):
        operation_path = os.path.join(os.path.dirname(__file__), "items.csv")
        try:
            with open(operation_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                reader = list(reader)
                if len(reader) != 6:  # Здесь идет проверка на количество строк в файле
                    raise InstantiateCSVError
                for i in range(1, len(reader)):
                    new_item = Item(reader[i][0], float(reader[i][1]), int(reader[i][2]))
                    Item.all.append(new_item)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        except InstantiateCSVError as ex:
            print(ex.message)

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:  # Тут можно сделать короче, но задание просит именно проверку на длинну
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


class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Файл item.csv поврежден'
