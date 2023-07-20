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

# class LanguageMixin:
#     """Миксин для хранения и изменения раскладки клавиатуры
#     (язык по умолчанию - английский)"""
#     SUPPORTED_LANGUAGES = ('EN', 'RU')
#
#     @property
#     def language(self) -> str:
#         """Возвращает текущий язык"""
#         return self.language
#
#     @language.setter
#     def language(self, value) -> None:
#         if value.upper() not in self.SUPPORTED_LANGUAGES:
#             raise ValueError('Unsupported language')
#         self.language = value
#
#     def change_lang(self):
#         current_language_index = self.SUPPORTED_LANGUAGES.index(self.language)
#         next_lang_index = (current_language_index + 1) % len(self.SUPPORTED_LANGUAGES)
#         self.language = self.SUPPORTED_LANGUAGES[next_lang_index]
#
#
# class Keyboard(Item, LanguageMixin):
#     """Подкласс для представления клавиатуры в магазине
#     с дополнительным функционалом по хранению и изменению раскладки клавиатуры"""
#
#     def __init__(self, name: str, price: float, quantity: int, language: str) -> None:
#         """
#         Инициализирует экземпляр класса Keyboard
#         :param name: Название клавиатуры
#         :param price: Цена клавиатуры
#         :param quantity: Количество клавиатур в магазине
#         :param language: Раскладка клавиатуры
#         """
#         super().__init__(name=name, price=price, quantity=quantity)
#         self.language = language
