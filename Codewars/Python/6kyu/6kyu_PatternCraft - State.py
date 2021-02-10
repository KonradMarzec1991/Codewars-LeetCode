class SiegeState:
    def __init__(self):
        pass  # your code here


class TankState:
    def __init__(self):
        pass  # your code here


class Tank:
    def __init__(self):
        self.state = TankState()

    def can_move(self):
        if self.state.__class__.__name__ == 'TankState':
            return True
        return False

    def damage(self):
        if self.state.__class__.__name__ == 'TankState':
            return 5
        return 20


# Great solution from CW
class SiegeState1:
    def __init__(self):
        self.canMove = False
        self.damage = 20


class TankState1:
    def __init__(self):
        self.canMove = True
        self.damage = 5


class Tank1:
    def __init__(self):
        self.state = TankState()

    def can_move(self):
        return self.state.canMove

    def damage(self):
        return self.state.damage
