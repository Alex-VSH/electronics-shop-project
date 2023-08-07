"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone

item1 = Item("Планшет", 30000, 20)
item2 = Item("Смарт-часы", 5000, 40)
item3 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 13", 80_000, 10, 4)


def test_repr():
    assert item3.__repr__() == "Item('Смартфон', 10000, 20)"
    assert item1.__repr__() == "Item('Планшет', 30000, 20)"


def test_str():
    assert item1.__str__() == 'Планшет'
    assert item2.__str__() == 'Смарт-часы'


def test_calculate_total_price():
    assert item1.calculate_total_price() == 600000
    assert item2.calculate_total_price() == 200000


def test_apply_discount():
    Item.pay_rate = 0.7
    item1.apply_discount()
    assert item1.price == 21000.0


def test_string_to_number():
    assert Item.string_to_number('2') == 2


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item_test = Item.all[3]
    assert item_test.name == 'Мышка'
    assert item_test.price == 50.0
    assert item_test.quantity == 5


def test_name():
    item1.name = "Печь"
    assert item1.name == "Печь"
    item1.name = 'Микроволновка'
    assert item1.name == 'Микроволно'


def test_add():
    assert phone1 + item1 == 30
    assert phone1 + item2 == 50
    with pytest.raises(Exception):
        phone1 + 10  # ValueError('Объект не класса Item или Phone')
