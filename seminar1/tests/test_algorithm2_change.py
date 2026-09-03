"""
Тесты для алгоритма 2: Жадный размен монет
"""

import pytest
from tasks.algorithm2_change import greedy_change


class TestGreedyChange:
    def test_empty_amount(self):
        assert greedy_change([25, 10, 5, 1], 0) == []
    
    def test_standard_coins(self):
        result = greedy_change([25, 10, 5, 1], 41)
        expected = [25, 10, 5, 1]
        assert result == expected
    
    def test_exact_amount(self):
        result = greedy_change([10, 5, 1], 15)
        assert sum(result) == 15
    
    def test_impossible(self):
        assert greedy_change([10, 5], 7) is None
    
    def test_single_coin(self):
        result = greedy_change([5], 15)
        assert result == [5, 5, 5]
    
    def test_large_amount(self):
        result = greedy_change([25, 10, 5, 1], 63)
        assert sum(result) == 63
    
    def test_greedy_not_optimal(self):
        """Демонстрация того, что жадный алгоритм не всегда оптимален"""
        result = greedy_change([1, 3, 4], 6)
        # Жадный даёт 4+1+1 (3 монеты)
        assert result == [4, 1, 1]
        # Оптимально было бы 3+3 (2 монеты)
        assert len(result) > 2
