def string_letter_count(s):
    d, s = {}, s.lower()
    for letter in s:
        if letter.isalpha():
            d[letter] = d.get(letter, 0) + 1
    return ''.join([f'{v}{k}' for k, v in sorted(d.items())]) if d else ''


print(string_letter_count("This is a test sentence."))