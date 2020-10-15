def remove_duplicate_ids(obj):
    new_obj = {
        k: obj[k] for k in sorted(
            obj.keys(), key=lambda x: int(x), reverse=True
        )}
    forbidden_letters = []
    for k, v in new_obj.items():
        final_arr = []
        for item in v:
            if item not in forbidden_letters:
                final_arr.append(item)
                forbidden_letters.append(item)
        new_obj[k] = final_arr
    return {
        k: new_obj[k] for k in sorted(
            new_obj.keys(), key=lambda x: int(x)
        )}