import pytest

from src.phone import Phone
from src.item import Item

item1 = Item("Планшет", 30000, 20)
phone1 = Phone("iPhone 13", 80_000, 10, 4)


def test_repr():
    assert repr(phone1) == "Phone('iPhone 13', 80000, 10, 4)"


def test_number_of_sim_setter():
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2
    with pytest.raises(Exception):
        phone1.number_of_sim = 0  # ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
