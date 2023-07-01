from src.item import Item

item = Item("Smartphone", 14999, 13)


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


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('1') == 1
    assert Item.string_to_number('13.5') == 13


def test_repr():
    assert repr(item) == "Item('Smartphone', 7499.5, 13)"


def test_str():
    assert str(item) == 'Smartphone'
