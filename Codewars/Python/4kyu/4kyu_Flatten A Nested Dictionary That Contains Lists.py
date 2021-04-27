def flatten(x):
    temp = {}
    for k, v in x.items():
        if isinstance(v, list):
            temp.update(flatten({f'{k}[{idx}]': val for idx, val in enumerate(v)}))
        elif isinstance(v, dict):
            temp.update(flatten({f'{k}.{key}': val for key, val in v.items()}))
        else:
            temp[k] = v
    return temp
