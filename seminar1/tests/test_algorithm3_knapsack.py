"""
Тесты для алгоритма 3: Дробный рюкзак
"""

import pytest
from tasks.algorithm3_knapsack import fractional_knapsack


class TestFractionalKnapsack:
    def test_sample(self):
        items = [(60, 10), (100, 20), (120, 30)]
        capacity = 50
        result = fractional_knapsack(items, capacity)
        assert abs(result - 240.0) < 1e-9
    
    def test_empty_items(self):
        assert fractional_knapsack([], 10) == 0.0
    
    def test_zero_capacity(self):
        items = [(10, 5), (20, 10)]
        assert fractional_knapsack(items, 0) == 0.0
    
    def test_partial_item(self):
        items = [(100, 10)]
        capacity = 5
        result = fractional_knapsack(items, capacity)
        assert abs(result - 50.0) < 1e-9
    
    def test_multiple_partial(self):
        items = [(10, 2), (100, 10)]
        capacity = 2
        result = fractional_knapsack(items, capacity)
        assert abs(result - 20.0) < 1e-9
    
    def test_exact_capacity(self):
        items = [(30, 5), (40, 10), (50, 15)]
        capacity = 30
        result = fractional_knapsack(items, capacity)
        assert abs(result - 120.0) < 1e-9
    
    def test_high_density_first(self):
        items = [(100, 10), (60, 20)]
        capacity = 15
        result = fractional_knapsack(items, capacity)
        assert abs(result - 115.0) < 1e-9
