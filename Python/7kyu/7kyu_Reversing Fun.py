# CodeWars Reversing Fun
def reverse_fun(n):
    n = n[::-1]  # 1
    k = 1
    for _ in range(k, len(n)):
        first = n[:k]
        second = n[k:]
        n = first + second[::-1]
        k += 1
    return n