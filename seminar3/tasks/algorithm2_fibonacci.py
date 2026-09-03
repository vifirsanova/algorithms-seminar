"""
Алгоритм 2: Числа Фибоначчи с мемоизацией
"""

from typing import Dict


def fibonacci(n: int, memo: Dict[int, int] = None) -> int:
    """
    Вычисляет n-е число Фибоначчи с использованием мемоизации.
    
    Аргументы:
        n: Индекс числа Фибоначчи (неотрицательный)
        memo: Словарь для кэширования результатов
        
    Возвращает:
        n-е число Фибоначчи
        
    Сложность:
        Время: O(n)
        Память: O(n) (словарь + стек вызовов)
        
    Примеры:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(6)
        8
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
