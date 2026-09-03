"""
Задачи семинара: Рекурсия
"""

from .task1_errors import factorial, factorial_safe
from .task2_recursion import sum_recursive, sum_recursive_opt
from .algorithm1_binary_search import binary_search
from .algorithm2_fibonacci import fibonacci
from .algorithm3_tree_traversal import Node, inorder_traversal

__all__ = [
    'factorial',
    'factorial_safe',
    'sum_recursive',
    'sum_recursive_opt',
    'binary_search',
    'fibonacci',
    'Node',
    'inorder_traversal',
]
