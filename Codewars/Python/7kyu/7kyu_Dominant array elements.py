def solve(arr):
    output = []
    for i in range(len(arr)):
        curr_val = arr[i]
        curr_arr = arr[i+1:]
        if all(curr_val > i for i in curr_arr):
            output.append(curr_val)
    return output
