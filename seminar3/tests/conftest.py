"""
Фикстуры для тестов
"""

import pytest
from tasks.task1_errors import factorial, factorial_safe
from tasks.task2_recursion import sum_recursive, sum_recursive_opt
from tasks.algorithm3_tree_traversal import Node


@pytest.fixture
def sample_tree():
    """Бинарное дерево для тестов"""
    #       2
    #      / \
    #     1   3
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    return root


@pytest.fixture
def large_tree():
    """Большое дерево для тестов"""
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    return root
