"""
Задачи семинара: Базовые структуры данных
"""

from .task1_errors import remove_evens, remove_evens_new
from .task2_stack import Stack, is_valid_parentheses
from .algorithm1_stack import Stack as StackAlgo
from .algorithm2_queue import Queue
from .algorithm3_linkedlist import DoublyLinkedList

__all__ = [
    'remove_evens',
    'remove_evens_new',
    'Stack',
    'is_valid_parentheses',
    'StackAlgo',
    'Queue',
    'DoublyLinkedList',
]
