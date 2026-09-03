"""
Алгоритм 3: Двусвязный список
"""

from typing import Optional, List


class Node:
    """
    Узел двусвязного списка.
    """
    
    def __init__(self, value: int):
        self.value: int = value
        self.next: Optional['Node'] = None
        self.prev: Optional['Node'] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class DoublyLinkedList:
    """
    Класс, реализующий двусвязный список.
    
    Временная сложность:
        - append: O(1)
        - prepend: O(1)
        - insert: O(n) (поиск позиции)
        - delete: O(n) (поиск элемента)
        - find: O(n)
        - __len__: O(1)
    
    Пространственная сложность: O(n), где n — количество элементов
    """
    
    def __init__(self):
        """Инициализация пустого списка."""
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: int) -> None:
        """
        Добавляет элемент в конец списка.
        
        Сложность: O(1)
        """
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.prev = self._tail
            self._tail.next = node
            self._tail = node
        self._size += 1
    
    def prepend(self, value: int) -> None:
        """
        Добавляет элемент в начало списка.
        
        Сложность: O(1)
        """
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1
    
    def insert(self, index: int, value: int) -> None:
        """
        Вставляет элемент на указанную позицию.
        
        Аргументы:
            index: Индекс для вставки (0-based)
            value: Вставляемое значение
            
        Исключения:
            IndexError: если индекс вне допустимого диапазона
            
        Сложность: O(n)
        """
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        
        if index == 0:
            self.prepend(value)
            return
        
        if index == self._size:
            self.append(value)
            return
        
        current = self._head
        for _ in range(index):
            current = current.next
        
        node = Node(value)
        node.prev = current.prev
        node.next = current
        current.prev.next = node
        current.prev = node
        self._size += 1
    
    def delete(self, value: int) -> bool:
        """
        Удаляет первое найденное вхождение элемента.
        
        Аргументы:
            value: Значение для удаления
            
        Возвращает:
            True, если элемент был удалён, иначе False
            
        Сложность: O(n)
        """
        current = self._head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail = current.prev
                
                self._size -= 1
                return True
            current = current.next
        return False
    
    def find(self, value: int) -> Optional[Node]:
        """
        Ищет элемент по значению.
        
        Аргументы:
            value: Искомое значение
            
        Возвращает:
            Узел с найденным значением или None
            
        Сложность: O(n)
        """
        current = self._head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def to_list(self) -> List[int]:
        """
        Преобразует список в обычный список Python.
        
        Сложность: O(n)
        """
        result = []
        current = self._head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def __len__(self) -> int:
        """Возвращает количество элементов."""
        return self._size
    
    def __repr__(self) -> str:
        return f"DoublyLinkedList({self.to_list()})"
