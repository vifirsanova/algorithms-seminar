"""
Алгоритм 1: Бинарный поиск (рекурсивная реализация)
"""

from typing import List, Optional


def binary_search(arr: List[int], target: int, left: int = 0, right: Optional[int] = None) -> int:
    """
    Выполняет бинарный поиск в отсортированном списке.
    
    Аргументы:
        arr: Отсортированный список целых чисел
        target: Искомое значение
        left: Левая граница поиска
        right: Правая граница поиска
        
    Возвращает:
        Индекс найденного элемента или -1, если элемент не найден
        
    Сложность:
        Время: O(log n)
        Память: O(log n) (глубина рекурсии)
        
    Примеры:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
