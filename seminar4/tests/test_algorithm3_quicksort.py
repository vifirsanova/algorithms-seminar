"""
Тесты для задачи 3: Быстрая сортировка
"""

import pytest
from tasks.algorithm3_quicksort import quick_sort


class TestQuickSort:
    def test_empty(self):
        assert quick_sort([]) == []
    
    def test_single(self):
        assert quick_sort([1]) == [1]
    
    def test_reverse(self):
        assert quick_sort([3, 2, 1]) == [1, 2, 3]
    
    def test_sorted(self):
        assert quick_sort([1, 2, 3]) == [1, 2, 3]
    
    def test_unsorted(self):
        assert quick_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    
    def test_negative(self):
        assert quick_sort([-1, -5, 0, 3]) == [-5, -1, 0, 3]
    
    def test_duplicates(self):
        assert quick_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]
