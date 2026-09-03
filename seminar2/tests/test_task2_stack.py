"""
Тесты для задачи 2: Реализация стека
"""

import pytest
from tasks.task2_stack import Stack, is_valid_parentheses


class TestStack:
    def test_empty(self):
        stack = Stack()
        assert stack.is_empty() is True
        assert len(stack) == 0
    
    def test_push(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.is_empty() is False
        assert len(stack) == 3
    
    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty() is True
        assert len(stack) == 0
    
    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.peek() == 3
        assert len(stack) == 3
        stack.pop()
        assert stack.peek() == 2
    
    def test_pop_empty(self):
        stack = Stack()
        with pytest.raises(IndexError, match="pop from empty stack"):
            stack.pop()
    
    def test_peek_empty(self):
        stack = Stack()
        with pytest.raises(IndexError, match="peek from empty stack"):
            stack.peek()


class TestValidParentheses:
    def test_empty(self):
        assert is_valid_parentheses("") is True
    
    def test_simple(self):
        assert is_valid_parentheses("()") is True
        assert is_valid_parentheses("()[]{}") is True
    
    def test_nested(self):
        assert is_valid_parentheses("((()))") is True
        assert is_valid_parentheses("{[]}") is True
    
    def test_invalid(self):
        assert is_valid_parentheses("(]") is False
        assert is_valid_parentheses("([)]") is False
        assert is_valid_parentheses("((())") is False
        assert is_valid_parentheses(")(") is False
        assert is_valid_parentheses("([)]") is False
    
    def test_complex_valid(self):
        assert is_valid_parentheses("({[]})") is True
        assert is_valid_parentheses("(){}[]") is True
        assert is_valid_parentheses("{[()]}") is True
