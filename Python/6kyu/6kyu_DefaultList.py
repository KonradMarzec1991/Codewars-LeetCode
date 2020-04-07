class DefaultList(list):
    def __init__(self, sequence, default):
        super().__init__(sequence)
        self.default = default

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except:
            return self.default