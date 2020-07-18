def solve(s):
    lower_count = sum(map(str.islower, s))
    upper_count = sum(map(str.isupper, s))
    return s.lower() if lower_count >= upper_count else s.upper()