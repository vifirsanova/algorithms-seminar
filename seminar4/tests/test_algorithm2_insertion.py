"""
Тесты для задачи 2: Сортировка вставками
"""

import pytest
from tasks.algorithm2_insertion import insertion_sort


class TestInsertionSort:
    def test_empty(self):
        assert insertion_sort([]) == []
    
    def test_single(self):
        assert insertion_sort([1]) == [1]
    
    def test_reverse(self):
        assert insertion_sort([3, 2, 1]) == [1, 2, 3]
    
    def test_sorted(self):
        assert insertion_sort([1, 2, 3]) == [1, 2, 3]
    
    def test_unsorted(self):
        assert insertion_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    
    def test_negative(self):
        assert insertion_sort([-1, -5, 0, 3]) == [-5, -1, 0, 3]
    
    def test_duplicates(self):
        assert insertion_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]
