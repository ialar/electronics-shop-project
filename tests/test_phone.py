import pytest


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 115000, 7, 1)"


def test_str(phone1):
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim(phone1):
    assert phone1.number_of_sim == 1
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


# noinspection PyStatementEffect
def test_add(item1, phone1):
    assert item1 + item1 == 40
    assert phone1 + phone1 == 14
    assert phone1 + item1 == 27
    assert item1 + phone1 == 27

    with pytest.raises(TypeError):
        phone1 + 'alien object'
