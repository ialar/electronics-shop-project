import pytest
from src.item import Item


@pytest.fixture
def new_name():
    return Item("Холодильник", 20000, 30)
