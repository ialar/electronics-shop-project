import pytest

from src.config import CSV_PATH_2, CSV_PATH_3
from src.instantiate_csv_error import InstantiateCSVError
from src.item import Item

item = Item('Smartphone', 14999, 13)


def test_calculate_total_price():
    assert item.calculate_total_price() == 194987


def test_apply_discount():
    assert item.price == 14999

    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 7499.5


def test_name(new_name):
    new_name.name = 'СуперСмартфон'
    assert new_name.name == 'СуперСмарт'


def test_string_to_number():
    assert Item.string_to_number('1') == 1
    assert Item.string_to_number('13.5') == 13


def test_repr(item1):
    assert repr(item) == "Item('Smartphone', 7499.5, 13)"
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1):
    assert str(item) == 'Smartphone'
    assert str(item1) == 'Смартфон'


# noinspection PyStatementEffect
def test_add(item1, phone1):
    assert item1 + phone1 == 27
    assert phone1 + item1 == 27
    assert item1 + item1 == 40
    assert phone1 + phone1 == 14

    with pytest.raises(TypeError):
        item1 + 'alien object'


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(CSV_PATH_2)


def test_instantiate_from_csv_file_corrupted():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(CSV_PATH_3)
