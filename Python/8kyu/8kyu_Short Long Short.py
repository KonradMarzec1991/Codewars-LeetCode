def solution(a, b):
    long = a if len(a) > len(b) else b
    short = a if len(a) < len(b) else b
    return f'{short}{long}{short}'
