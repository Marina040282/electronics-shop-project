"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from electronics_shop_project.src.item import Item

def test_calculate_total_price():
    assert Item.calculate_total_price(20000, 5) == 10000


def test_apply_discount():
    assert Item.apply_discount(0.8, 10000) == 8000
