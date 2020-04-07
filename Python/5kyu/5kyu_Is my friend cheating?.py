def removNb(n):
    n_sum, results = n * (n + 1) / 2 + 1, []

    def find_divisors(num):
        import math
        result = [1, num]
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                if num / i == i:
                    result.append(i)
                else:
                    result.append(i)
                    result.append(num / i)
        return sorted(map(int, result))

    divs = find_divisors(n_sum)
    for i in range(len(divs)):
        for j in range(len(divs)):
            one, two = divs[i] - 1, divs[j] - 1
            if one < n and two < n and one * two == n_sum - one - two - 1:
                results.append((one, two))
    return results