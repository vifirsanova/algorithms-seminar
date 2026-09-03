"""
Тесты для задачи 2: Выбор мероприятий
"""

import pytest
from tasks.task2_events import select_events


class TestSelectEvents:
    def test_empty(self):
        assert select_events([]) == []
    
    def test_single(self):
        assert select_events([(1, 2)]) == [(1, 2)]
    
    def test_sample(self):
        events = [
            (1, 4), (3, 5), (0, 6),
            (5, 7), (8, 9), (5, 9)
        ]
        expected = [(1, 4), (5, 7), (8, 9)]
        assert select_events(events) == expected
    
    def test_optimal_choice(self):
        events = [(1, 10), (2, 3), (3, 4), (4, 5)]
        result = select_events(events)
        assert len(result) == 3
        assert result == [(2, 3), (3, 4), (4, 5)]
    
    def test_adjacent(self):
        events = [(0, 1), (1, 2), (2, 3)]
        expected = [(0, 1), (1, 2), (2, 3)]
        assert select_events(events) == expected
    
    def test_overlapping(self):
        events = [(0, 5), (1, 2), (3, 4)]
        result = select_events(events)
        assert len(result) == 2
    
    def test_unsorted_input(self):
        events = [(5, 7), (1, 4), (8, 9), (3, 5)]
        expected = [(1, 4), (5, 7), (8, 9)]
        assert select_events(events) == expected
