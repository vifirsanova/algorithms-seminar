"""
Тесты для задачи 1: Поиск ошибок в коде
"""

import pytest
from tasks.task1_errors import remove_evens, remove_evens_new


class TestRemoveEvens:
    def test_empty(self):
        assert remove_evens([]) == []
        assert remove_evens_new([]) == []
    
    def test_no_evens(self):
        assert remove_evens([1, 3, 5]) == [1, 3, 5]
        assert remove_evens_new([1, 3, 5]) == [1, 3, 5]
    
    def test_all_evens(self):
        assert remove_evens([2, 4, 6]) == []
        assert remove_evens_new([2, 4, 6]) == []
    
    def test_mixed(self):
        assert remove_evens([1, 2, 3, 4, 5]) == [1, 3, 5]
        assert remove_evens_new([1, 2, 3, 4, 5]) == [1, 3, 5]
    
    def test_mixed2(self):
        assert remove_evens([2, 3, 4, 5, 6]) == [3, 5]
        assert remove_evens_new([2, 3, 4, 5, 6]) == [3, 5]
    
    def test_range(self):
        assert remove_evens(list(range(10))) == [1, 3, 5, 7, 9]
        assert remove_evens_new(list(range(10))) == [1, 3, 5, 7, 9]
    
    def test_negative_numbers(self):
        assert remove_evens([-2, -1, 0, 1, 2]) == [-1, 1]
        assert remove_evens_new([-2, -1, 0, 1, 2]) == [-1, 1]
