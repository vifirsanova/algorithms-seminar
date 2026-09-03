"""
Фикстуры для тестов
"""

import pytest


@pytest.fixture
def empty_stack():
    """Пустой стек для тестов"""
    from tasks.task2_stack import Stack
    return Stack()


@pytest.fixture
def filled_stack():
    """Стек с тремя элементами"""
    from tasks.task2_stack import Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack
