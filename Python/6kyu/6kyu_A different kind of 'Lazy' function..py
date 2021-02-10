class lazy:
    def __init__(self, freq):
        self.freq = freq
        self.counter = -1

    def is_call_func(self):
        if self.freq == -1:
            return False

        if self.counter <= 0:
            return True
        if self.freq > 0:
            return self.counter % self.freq == 0
        if self.freq < 0:
            return (self.counter + 1) % abs(self.freq) != 0

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            self.counter += 1
            if self.is_call_func():
                return fn(*args, **kwargs)
            return None
        return wrapper
