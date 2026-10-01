import heapq


def kmerge(streams):
    """Слить k отсортированных списков в один отсортированный.

    Args:
        streams: список списков. Каждый вложенный список уже отсортирован
            по возрастанию. Списки могут быть пустыми, их количество
            может быть любым.

    Returns:
        Один список, содержащий все элементы из streams в отсортированном
        по возрастанию порядке.
    """
    # heap <- min-heap
    # Каждый элемент кучи — это тройка (значение, id потока, индекс).
    # Значение — то, по чему сравниваем. id и индекс нужны, чтобы
    # после извлечения понять, откуда пришёл элемент и куда двигаться дальше.
    heap = []

    # for each stream:
    #     push(heap, (stream.head, stream.id))
    # Кладём в кучу по одному первому элементу от каждого потока.
    # Пустые потоки пропускаем — у них нет головы.
    for stream_id, stream in enumerate(streams):
        if stream:
            heapq.heappush(heap, (stream[0], stream_id, 0))

    # output <- []
    result = []

    # while heap not empty:
    while heap:
        # (value, id) <- pop(heap)
        # Извлекаем минимальную голову среди всех потоков.
        # Это и есть следующий элемент в итоговом порядке.
        value, stream_id, idx = heapq.heappop(heap)
        result.append(value)

        # if streams[id] has next:
        #     push(heap, (streams[id].next, id))
        # Подтягиваем следующий элемент из того же потока,
        # чтобы он мог участвовать в следующих сравнениях.
        next_idx = idx + 1
        if next_idx < len(streams[stream_id]):
            next_value = streams[stream_id][next_idx]
            heapq.heappush(heap, (next_value, stream_id, next_idx))

    # return output
    return result
