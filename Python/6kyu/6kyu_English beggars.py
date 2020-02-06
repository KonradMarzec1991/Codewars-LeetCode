

def beggars(values, n):
    from queue import Queue
    if n == 0:
        return []
    q = Queue(maxsize=len(values))
    for val in values:
        q.put(val)
    output_list = [0]*n
    index = 0
    while not q.empty():
        output_list[index] += q.get()
        index += 1
        if index > len(output_list) - 1:
            index = 0
    return output_list
