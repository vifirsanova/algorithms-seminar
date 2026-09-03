"""
Тесты для алгоритма 1: Activity Selection
"""

import pytest
from tasks.algorithm1_activity import activity_selection


class TestActivitySelection:
    def test_empty(self):
        assert activity_selection([]) == []
    
    def test_single(self):
        assert activity_selection([(1, 2)]) == [(1, 2)]
    
    def test_sample(self):
        activities = [
            (1, 4), (3, 5), (0, 6),
            (5, 7), (8, 9), (5, 9)
        ]
        expected = [(1, 4), (5, 7), (8, 9)]
        assert activity_selection(activities) == expected
    
    def test_optimal_choice(self):
        activities = [(1, 10), (2, 3), (3, 4), (4, 5)]
        result = activity_selection(activities)
        assert len(result) == 3
        assert result == [(2, 3), (3, 4), (4, 5)]
    
    def test_adjacent(self):
        activities = [(0, 1), (1, 2), (2, 3)]
        expected = [(0, 1), (1, 2), (2, 3)]
        assert activity_selection(activities) == expected
    
    def test_unsorted_input(self):
        activities = [(5, 7), (1, 4), (8, 9), (3, 5)]
        expected = [(1, 4), (5, 7), (8, 9)]
        assert activity_selection(activities) == expected
