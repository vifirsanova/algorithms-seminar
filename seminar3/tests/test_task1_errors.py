"""
Тесты для задачи 1: Поиск ошибок в рекурсивной функции
"""

import pytest
from tasks.task1_errors import factorial, factorial_safe


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1
        assert factorial_safe(0) == 1
    
    def test_one(self):
        assert factorial(1) == 1
        assert factorial_safe(1) == 1
    
    def test_small(self):
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(5) == 120
        
        assert factorial_safe(2) == 2
        assert factorial_safe(3) == 6
        assert factorial_safe(5) == 120
    
    def test_large(self):
        assert factorial(10) == 3628800
        assert factorial_safe(10) == 3628800
    
    def test_negative(self):
        with pytest.raises(ValueError, match="non-negative"):
            factorial(-1)
        
        with pytest.raises(ValueError, match="non-negative"):
            factorial_safe(-1)
    
    def test_too_deep(self):
        with pytest.raises(ValueError, match="too large"):
            factorial_safe(1000)
