class DictModified(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._keys = sorted(self.keys())

    def __getitem__(self, partial):
        for k in self._keys:
            if k.startswith(partial):
                return super().__getitem__(k)

partial_keys = DictModified