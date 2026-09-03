"""
Тесты для задачи 1: Проверка дубликатов
"""

import pytest
from tasks.task1_duplicates import has_duplicates


class TestHasDuplicates:
    def test_empty(self):
        assert has_duplicates([]) is False
    
    def test_single(self):
        assert has_duplicates([1]) is False
    
    def test_unique(self):
        assert has_duplicates([1, 2, 3, 4, 5]) is False
    
    def test_duplicate(self):
        assert has_duplicates([1, 2, 1]) is True
        assert has_duplicates([5, 5]) is True
    
    def test_duplicate_not_adjacent(self):
        assert has_duplicates([1, 2, 3, 4, 2, 5]) is True
    
    def test_large_unique(self):
        data = list(range(100_000))
        assert has_duplicates(data) is False
    
    def test_large_with_duplicate(self):
        data = list(range(99_999)) + [0]
        assert has_duplicates(data) is True
    
    def test_negative_numbers(self):
        assert has_duplicates([-1, -2, -1]) is True
        assert has_duplicates([-1, -2, -3]) is False
