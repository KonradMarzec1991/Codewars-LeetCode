class RememberMeta(type):
    instances = dict()

    def __getitem__(self, *key):
        if isinstance(*key, int):
            return RememberMeta.instances.get(key, None)
        return RememberMeta.instances.get(tuple(*key), None)

    def __len__(self):
        return len(self.instances)

    def __iter__(self):
        for key in self.instances.keys():
            yield key

    def __call__(cls, *args):
        existing_instance = RememberMeta.instances.get(tuple(args), None)
        if existing_instance is None:
            RememberMeta.instances[tuple(args)] = super().__call__(*args)
        return RememberMeta.instances[tuple(args)]


def remember(cls):
    return RememberMeta(
        cls.__name__,
        cls.__bases__,
        dict(cls.__dict__)
    )


@remember
class A:
   def __init__(self, x, y=0, z=0):
     pass
