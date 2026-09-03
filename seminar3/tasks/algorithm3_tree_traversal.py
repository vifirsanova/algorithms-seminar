"""
Алгоритм 3: Обход бинарного дерева (in-order)
"""

from typing import List, Optional


class Node:
    """
    Узел бинарного дерева.
    """
    
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


def inorder_traversal(root: Optional[Node]) -> List[int]:
    """
    Выполняет in-order обход бинарного дерева.
    
    Аргументы:
        root: Корень дерева
        
    Возвращает:
        Список значений узлов в порядке in-order обхода
        
    Сложность:
        Время: O(n)
        Память: O(n) (результат + стек вызовов)
        
    Примеры:
        >>> root = Node(2)
        >>> root.left = Node(1)
        >>> root.right = Node(3)
        >>> inorder_traversal(root)
        [1, 2, 3]
    """
    if root is None:
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))
    result.append(root.value)
    result.extend(inorder_traversal(root.right))
    return result
