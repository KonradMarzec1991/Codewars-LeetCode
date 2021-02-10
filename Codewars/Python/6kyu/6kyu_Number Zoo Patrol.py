def find_missing_number(numbers):
    if not numbers: return 1
    l = max(numbers)
    nums = l*(l+1)/2
    diff = nums - sum(numbers)
    if diff == 0:
        return l + 1
    return int(diff)