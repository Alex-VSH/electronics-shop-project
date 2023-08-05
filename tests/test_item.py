"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Планшет", 30000, 20)
item2 = Item("Смарт-часы", 5000, 40)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 600000
    assert item2.calculate_total_price() == 200000


def test_apply_discount():
    Item.pay_rate = 0.7
    item1.apply_discount()
    assert item1.price == 21000.0


def test_string_to_number():
    assert Item.string_to_number('2') == 2


def test_name():
    item1.name = "Печь"
    assert item1.name == "Печь"
    item1.name = 'Микроволновка'
    assert item1.name == 'Микроволно'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item_test = Item.all[3]
    assert item_test.name == 'Мышка'
    assert item_test.price == 50.0
    assert item_test.quantity == 5
