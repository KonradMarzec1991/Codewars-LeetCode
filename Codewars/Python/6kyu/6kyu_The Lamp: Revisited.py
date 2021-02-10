class Lamp:
    def __init__(self, color):
        self.color = color
        self.on = False

    def toggle_switch(self):
        self.on = not self.on

    def get_on(self):
        if self.on:
            return 'on'
        return 'off'

    def state(self):
        return f'The lamp is {self.get_on()}.'