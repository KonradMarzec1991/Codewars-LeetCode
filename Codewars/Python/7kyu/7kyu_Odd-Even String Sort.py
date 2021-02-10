def sort_my_string(S):

    new_s = ''
    new_s1 = ''

    for i, x in enumerate(S):
        if i%2 == 0:
            new_s += x
        else:
            new_s1 += x

    return f'{new_s} {new_s1}'


S = 'CodeWars'
print(S[::2])