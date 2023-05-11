"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from electronics_shop_project.src.item import Item


def test_calculate_total_price():
    assert Item.calculate_total_price(20000, 5) == 10000


def test_apply_discount():
    assert Item.apply_discount(0.8, 10000) == 8000


def test_string_to_number_1():
    assert Item.string_to_number('5') == 5


def test_string_to_number_2():
    assert Item.string_to_number('5.0') == 5


def test_string_to_number_3():
    assert Item.string_to_number('5.5') == 5


def test_name():
    assert Item.name == 'Смартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
