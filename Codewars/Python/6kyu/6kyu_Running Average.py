def running_average():
    self_arr = []

    def inner(num):
        self_arr.append(num)
        return round(sum(self_arr)/len(self_arr), 2)
    return inner
