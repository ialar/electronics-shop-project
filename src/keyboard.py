from src.item import Item


class MixinLanguage:
    """Миксин для хранения и изменения раскладки клавиатуры.
    Язык по умолчанию - английский."""
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self) -> str:
        """Возвращает текущий язык"""
        return self.__language

    def change_lang(self):
        """Возвращает измененный язык"""
        self.__language = 'RU' if self.language == 'EN' else 'EN'
        return self


class Keyboard(Item, MixinLanguage):
    """Подкласс для представления клавиатуры в магазине
    с дополнительным функционалом по хранению и изменению раскладки клавиатуры."""

    def __init__(self, name: str, price: float, quantity: int):
        """
        Инициализирует экземпляр класса Keyboard.
        :param name: Название клавиатуры.
        :param price: Цена клавиатуры.
        :param quantity: Количество клавиатур в магазине.
        """
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
