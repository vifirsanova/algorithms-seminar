"""
Алгоритм 1: Реализация стека
"""

from typing import List


class Stack:
    """
    Класс, реализующий стек (LIFO).
    
    Временная сложность всех операций: O(1)
    Пространственная сложность: O(n), где n — количество элементов
    """
    
    def __init__(self):
        """Инициализация пустого стека."""
        self._items: List[int] = []
    
    def push(self, x: int) -> None:
        """
        Добавляет элемент на вершину стека.
        
        Сложность: O(1) амортизированно
        """
        self._items.append(x)
    
    def pop(self) -> int:
        """
        Удаляет и возвращает элемент с вершины стека.
        
        Возвращает:
            Элемент с вершины стека
            
        Исключения:
            IndexError: если стек пуст
            
        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> int:
        """
        Возвращает элемент с вершины стека без удаления.
        
        Возвращает:
            Элемент с вершины стека
            
        Исключения:
            IndexError: если стек пуст
            
        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        
        Сложность: O(1)
        """
        return len(self._items) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке.
        
        Сложность: O(1)
        """
        return len(self._items)
    
    def __repr__(self) -> str:
        return f"Stack({self._items})"
