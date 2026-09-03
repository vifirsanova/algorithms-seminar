"""
Задачи семинара 1: Жадные алгоритмы
"""

from .task1_duplicates import has_duplicates
from .task2_events import select_events
from .algorithm1_activity import activity_selection
from .algorithm2_change import greedy_change
from .algorithm3_knapsack import fractional_knapsack

__all__ = [
    'has_duplicates',
    'select_events',
    'activity_selection',
    'greedy_change',
    'fractional_knapsack',
]
