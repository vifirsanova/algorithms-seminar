"""
Тесты для задачи 1: Поиск ошибок в сортировке
"""

import pytest
from tasks.task1_errors import bubble_sort, bubble_sort_opt


class TestBubbleSort:
    def test_empty(self):
        assert bubble_sort([]) == []
        assert bubble_sort_opt([]) == []
    
    def test_single(self):
        assert bubble_sort([1]) == [1]
        assert bubble_sort_opt([1]) == [1]
    
    def test_reverse(self):
        assert bubble_sort([3, 2, 1]) == [1, 2, 3]
        assert bubble_sort_opt([3, 2, 1]) == [1, 2, 3]
    
    def test_sorted(self):
        assert bubble_sort([1, 2, 3]) == [1, 2, 3]
        assert bubble_sort_opt([1, 2, 3]) == [1, 2, 3]
    
    def test_unsorted(self):
        assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
        assert bubble_sort_opt([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    
    def test_negative(self):
        assert bubble_sort([-1, -5, 0, 3]) == [-5, -1, 0, 3]
        assert bubble_sort_opt([-1, -5, 0, 3]) == [-5, -1, 0, 3]
    
    def test_duplicates(self):
        assert bubble_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]
        assert bubble_sort_opt([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]
