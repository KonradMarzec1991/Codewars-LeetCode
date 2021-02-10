class Dictionary:
    def __init__(self):
        self.data = {}

    def newentry(self, word, definition):
        self.data[word] = definition

    def look(self, key):
        if key in self.data:
            return self.data[key]
        return f"Can't find entry for {key}"
