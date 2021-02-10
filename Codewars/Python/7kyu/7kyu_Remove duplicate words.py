def remove_duplicate_words(s):
    from collections import OrderedDict
    return ' '.join(list(OrderedDict.fromkeys(s.split())))