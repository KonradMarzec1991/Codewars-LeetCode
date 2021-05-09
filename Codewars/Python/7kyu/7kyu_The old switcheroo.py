def vowel_2_index(string):
    return ''.join([str(i) if v in 'aeiouAEIOU' else v for i, v in enumerate(string, 1)])
