"""
Алгоритм 2: Реализация очереди
"""

from typing import List
from collections import deque


class Queue:
    """
    Класс, реализующий очередь (FIFO).
    
    Временная сложность всех операций: O(1)
    Пространственная сложность: O(n), где n — количество элементов
    """
    
    def __init__(self):
        """Инициализация пустой очереди."""
        self._items: deque = deque()
    
    def enqueue(self, x: int) -> None:
        """
        Добавляет элемент в конец очереди.
        
        Сложность: O(1)
        """
        self._items.append(x)
    
    def dequeue(self) -> int:
        """
        Удаляет и возвращает элемент из начала очереди.
        
        Возвращает:
            Элемент из начала очереди
            
        Исключения:
            IndexError: если очередь пуста
            
        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()
    
    def peek(self) -> int:
        """
        Возвращает элемент из начала очереди без удаления.
        
        Возвращает:
            Элемент из начала очереди
            
        Исключения:
            IndexError: если очередь пуста
            
        Сложность: O(1)
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]
    
    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь.
        
        Сложность: O(1)
        """
        return len(self._items) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди.
        
        Сложность: O(1)
        """
        return len(self._items)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"
