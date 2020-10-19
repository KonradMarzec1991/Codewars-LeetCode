def loneliest(strng):
    s = strng.strip()
    empty_lines = len(strng) - len(strng.replace(' ', ''))

    if not empty_lines:
        return list(strng)

    left_spaces, right_spaces = 0, 0
    previous_letter = s[0]
    letters = {}
    for ch in s[1:]:
        if ch != ' ':
            letters[previous_letter] = left_spaces + right_spaces
            previous_letter = ch
            left_spaces = right_spaces
            right_spaces = 0
        else:
            right_spaces += 1
    letters[previous_letter] = left_spaces + right_spaces

    max_spaces = letters[max(letters, key=letters.get)]
    max_letters = []
    for k in letters.keys():
        if letters[k] == max_spaces:
            max_letters.append(k)
    return max_letters
