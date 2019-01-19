def count(string):

    dict_string = {}

    for d in string:
        if d not in dict_string:
            dict_string[d] = 1
        else:
            dict_string[d] = dict_string.get(d) + 1

    return dict_string
