def even_chars(st):
    if len(st) < 2 or len(st) > 100:
        return "invalid string"
    else:
        return [v for i, v in enumerate(st, 1) if i % 2 == 0]


print(even_chars("a"))
print(even_chars("abcdefghijklm"))
print(even_chars("aBc_e9g*i-k$m"))