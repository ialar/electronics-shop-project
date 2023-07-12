import csv

from src.config import CSV_PATH


class Item:
    """Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Инициализирует экземпляр класса Item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """Репрезентация класса для отладки."""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Строковое представление объекта для пользователя (название товара)."""
        return f'{self.__name}'

    def __add__(self, other) -> int:
        """Возвращает результат сложения (по количеству товара в магазине)."""
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise TypeError('Складывать можно только объекты Item и дочерние от них.')

    @property
    def name(self):
        """Возвращает название товара."""
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        """Устанавливает новое название товара длиной не более 10 символов."""
        self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, csv_path=CSV_PATH):
        """Инициализирует экземпляры класса Item данными из CSV-файла."""
        with open(csv_path, 'r', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for i in reader:
                cls(i['name'], float(i['price']), cls.string_to_number(i['quantity']))

    @staticmethod
    def string_to_number(value: str):
        """Возвращает число из 'числа-строки'."""
        return int(float(value))

    def calculate_total_price(self) -> float:
        """Возвращает общую стоимость конкретного товара в магазине."""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price = self.price * self.pay_rate
