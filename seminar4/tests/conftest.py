"""
Фикстуры для тестов
"""

import pytest
from typing import List


@pytest.fixture
def empty_list() -> List[int]:
    """Пустой список"""
    return []


@pytest.fixture
def single_list() -> List[int]:
    """Список из одного элемента"""
    return [1]


@pytest.fixture
def sorted_list() -> List[int]:
    """Отсортированный список"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def unsorted_list() -> List[int]:
    """Неотсортированный список"""
    return [3, 5, 1, 4, 2]


@pytest.fixture
def reverse_list() -> List[int]:
    """Список в обратном порядке"""
    return [5, 4, 3, 2, 1]


@pytest.fixture
def list_with_duplicates() -> List[int]:
    """Список с дубликатами"""
    return [3, 1, 2, 1, 3, 2]


@pytest.fixture
def negative_list() -> List[int]:
    """Список с отрицательными числами"""
    return [-1, -5, 0, 3, -2]
