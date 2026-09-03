"""
Задача 1: Пузырьковая сортировка
Допиши код вместо ...
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Сортирует список пузырьковой сортировкой.
    
    Аргументы:
        arr: Список целых чисел
        
    Возвращает:
        Отсортированный список
        
    Пример:
        >>> bubble_sort([3, 2, 1])
        [1, 2, 3]
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        # TODO: внутренний цикл, границы n - 1 - i
        for j in range(...):
            # TODO: условие для обмена
            if ...:
                # TODO: поменять местами
                ...
                swapped = True
        # TODO: если не было обменов, выходим
        if ...:
            break
    
    return arr
