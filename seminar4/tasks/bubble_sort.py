def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        # последние i элементов уже на своих местах
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:   # обменов не было — массив отсортирован
            break
    return arr
