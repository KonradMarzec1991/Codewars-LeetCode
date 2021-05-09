def solution(args):
    string, i, arr = '', 0, []
    while args:
        arr.append(args.pop(0))
        if len(arr) == 1: continue
        else:
            if arr[-1] - arr[-2] == 1: continue
            else:
                if len(arr) <= 3:
                    string += str(arr.pop(0)) + ','
                    if len(arr) == 1: continue
                    elif arr[-1] - arr[-2] != 1:
                        string += str(arr.pop(0)) + ','
                else:
                    string += str(arr[0]) + '-' + str(arr[-2]) + ','
                    arr = [arr[-1]]
    if len(arr) < 3:
        for i in arr:
            string += str(i) + ','
        return string[:len(string)-1]
    else:
        string += str(arr[0]) + '-' + str(arr[-1])
        return string


# other
def solution2(args):
    args.append(0)
    list_range = []
    temp = []
    for index, item in enumerate(args[:-1]):
        if args[index+1] - args[index] == 1:
            temp.append(args[index])
            continue
        temp.append(args[index])
        if len(temp) == 1:
            list_range.append(f'{temp[0]}')
        if len(temp) == 2:
            list_range.append(f'{temp[0]}')
            list_range.append(f'{temp[1]}')
        if len(temp) > 2:
            list_range.append(f'{temp[0]}-{temp[len(temp)-1]}')
        temp = []

    return ','.join(list_range)
