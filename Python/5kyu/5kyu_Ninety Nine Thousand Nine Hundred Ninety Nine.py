num_dict = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
    70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'
}


def number_to_english(n):
    if not isinstance(n, int) or n < 0 or n > 99999:
        return ''
    if n in num_dict:
        if n >= 100:
            return num_dict[1] + ' ' + num_dict[n]
        else:
            return num_dict[n]

    n_len = len(str(n))
    if n_len > 4:
        div = 10 ** (n_len - 2)
    else:
        div = 10 ** (n_len - 1)

    p = n // div
    if div == 10:
        return num_dict[n - n % 10] + ' ' + num_dict[n % 10]
    else:
        if p not in num_dict:
            label_1 = num_dict[p - p % 10] + ' ' + num_dict[p % 10]
        else:
            label_1 = num_dict[p]
    if n % div == 0:
        return label_1 + ' ' + num_dict[div]
    return label_1 + ' ' + num_dict[div] + ' ' + number_to_english(n % div)
