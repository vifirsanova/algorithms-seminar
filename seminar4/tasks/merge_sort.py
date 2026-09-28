def merge_sort(arr):
    if len(arr) <= 1:          # база: 0 или 1 элемент уже отсортирован
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # сортируем левую половину
    right = merge_sort(arr[mid:])   # сортируем правую половину
    return merge(left, right)       # сливаем

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:     # берём меньший из двух
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])         # остаток left
    result.extend(right[j:])        # остаток right
    return result
