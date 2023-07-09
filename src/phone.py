from src.item import Item


class Phone(Item):
    """Подкласс для представления телефона в магазине
    с дополнительным атрибутом количества поддерживаемых SIM-карт."""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
            Создает экземпляр класса Phone.
            :param name: Название телефона.
            :param price: Цена телефона.
            :param quantity: Количество телефонов в магазине.
            :param number_of_sim: Количество поддерживаемых SIM-карт.
            """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Репрезентация класса для отладки."""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """Возвращает количество поддерживаемых сим-карт."""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Устанавливает количество поддерживаемых SIM-карт"""
        if value <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = value

    def __add__(self, other) -> int:
        """Возвращает результат сложения (по количеству товара в магазине)"""
        if not isinstance(other, Item):
            raise TypeError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
