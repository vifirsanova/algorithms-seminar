"""
Тесты для задачи 2: Рекурсивный обход списка
"""

import pytest
from tasks.task2_recursion import sum_recursive, sum_recursive_opt


class TestSumRecursive:
    def test_empty(self):
        assert sum_recursive([]) == 0
        assert sum_recursive_opt([]) == 0
    
    def test_single(self):
        assert sum_recursive([1]) == 1
        assert sum_recursive_opt([1]) == 1
    
    def test_small(self):
        assert sum_recursive([1, 2, 3]) == 6
        assert sum_recursive_opt([1, 2, 3]) == 6
    
    def test_negative(self):
        assert sum_recursive([-1, 1]) == 0
        assert sum_recursive_opt([-1, 1]) == 0
    
    def test_large(self):
        assert sum_recursive([10, 20, 30, 40]) == 100
        assert sum_recursive_opt([10, 20, 30, 40]) == 100
    
    def test_long(self):
        data = list(range(100))
        expected = 4950
        assert sum_recursive(data) == expected
        assert sum_recursive_opt(data) == expected
    
    def test_recursion_depth(self):
        # Проверяем, что функция не падает на больших данных
        data = list(range(500))
        assert sum_recursive_opt(data) == sum(data)
