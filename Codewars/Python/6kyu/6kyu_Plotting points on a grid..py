class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.arr = [[0] * self.width for _ in range(self.height)]

    def plot_point(self, x, y):
        self.arr[y-1][x-1] = 'X'

    @property
    def grid(self):
        my_str = ''
        for index, val in enumerate(self.arr):
            print(index)
            if index == self.height - 1:
                my_str += ''.join([str(j) for j in val])
            else:
                my_str += ''.join([str(j) for j in val]) + '\n'
        return my_str
