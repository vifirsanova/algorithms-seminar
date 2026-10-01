import heapq
import numpy as np


def top_k_search(embeddings, query, k):
    """Вернуть k ближайших векторов к запросу.

    Args:
        embeddings: np.ndarray формы (N, d). N векторов размерности d.
        query: np.ndarray формы (d,). Вектор запроса той же размерности.
        k: целое число, сколько ближайших векторов вернуть.

    Returns:
        Список из k пар (distance, index), отсортированный по возрастанию
        расстояния. distance — евклидово расстояние от вектора до query,
        index — его позиция в embeddings.

    Ограничение:
        Нельзя сортировать весь массив расстояний. Нужно использовать
        bounded heap размера k.
    """
    pass
