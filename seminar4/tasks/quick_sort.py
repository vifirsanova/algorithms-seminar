def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    # База рекурсии: подмассив из 0 или 1 элемента уже отсортирован
    if low < high:
        # p — индекс pivot после разбиения
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)    # сортируем левую часть
        quick_sort(arr, pi + 1, high)   # сортируем правую часть
    return arr

def partition(arr, low, high):
    pivot = arr[high]   # опорный элемент — последний в подмассиве
    i = low - 1         # граница «области меньше pivot»
    for j in range(low, high):
        if arr[j] < pivot:
            # расширяем область меньше pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # ставим pivot сразу после области меньших элементов
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1        # новый индекс pivot
