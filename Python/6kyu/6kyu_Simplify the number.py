def simplify(number):
    arr = [int(val) for val in str(number)]
    result, counter, last = [], 10, arr.pop()
    if last:
        result.append(str(last))
    for val in arr[::-1]:
        if val > 0:
            result.append(f'{val}*{counter}')
        counter *= 10
    return '+'.join(result[::-1])