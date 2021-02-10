# Time out
def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    timer, checkout, waiting = 0, customers[:n], customers[n:]
    while checkout:
        for index, value in enumerate(checkout):
            if checkout[index] == 0 and len(checkout) == 1:
                timer -= 1
                break
            checkout[index] -= 1
        for index, value in enumerate(checkout):
            if checkout[index] == 0:
                del checkout[index]
                if waiting:
                    checkout.insert(0, waiting.pop(0))
        timer += 1
    return timer


def super_queue_time(customers, n):
    tills = [0] * n
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)