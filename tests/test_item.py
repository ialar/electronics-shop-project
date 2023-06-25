from src.item import Item

item = Item("Smartphone", 14999, 13)


def test_calculate_total_price():
    assert item.calculate_total_price() == 194987


def test_apply_discount():
    assert item.price == 14999

    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 7499.5
