class SecureList:

    def __init__(self, messages):
        self.messages = list(messages)

    def __getitem__(self, item):
        return self.messages.pop(item)

    def __len__(self):
        return len(self.messages)

    def __repr__(self):
        temp, self.messages = self.messages, []
        return repr(temp)

    def __str__(self):
        temp, self.messages = self.messages, []
        return '{0}'.format(temp)