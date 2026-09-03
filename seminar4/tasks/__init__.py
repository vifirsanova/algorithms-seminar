"""
Задачи семинара: Сортировки
"""

from .task1_errors import bubble_sort, bubble_sort_opt
from .task2_sorting import insertion_sort
from .algorithm1_bubble import bubble_sort as bubble_algo
from .algorithm2_insertion import insertion_sort as insertion_algo
from .algorithm3_quicksort import quick_sort

__all__ = [
    'bubble_sort',
    'bubble_sort_opt',
    'insertion_sort',
    'bubble_algo',
    'insertion_algo',
    'quick_sort',
]