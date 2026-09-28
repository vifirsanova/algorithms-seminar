def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]     # элемент, который вставляем
        j = i - 1
        # сдвигаем большие элементы вправо, освобождая место для key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
