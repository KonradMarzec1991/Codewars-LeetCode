class Format:
    def __init__(self, tags=None):
        if tags is None:
            self._tags = list()
        else:
            self._tags = tags

    def __getattr__(self, item):
        return Format(self._tags + [item])

    def __call__(self, *args):
        values = ''.join(arg for arg in args)
        for tag in self._tags[::-1]:
            values = f'<{tag}>{values}</{tag}>'
        return values


formatter = Format()
