def merge_k_sorted_lists(lists):
    """
    Объединить k отсортированных массивов в один.
    """
    # TODO: реализовать
    pass

# Примеры:
assert merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], 
                             [2, 6]]) == \
       [1, 1, 2, 3, 4, 4, 5, 6]
assert merge_k_sorted_lists([[1], [2], [3]]) == [1, 2, 3]
assert merge_k_sorted_lists([]) == []
