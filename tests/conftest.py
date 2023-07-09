import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def new_name():
    return Item("СуперСмартфон", 20000, 30)


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 115000, 7, 1)
