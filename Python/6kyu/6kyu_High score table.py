class HighScoreTable:
    def __init__(self, ltg=3):
        self.ltg = ltg
        self.scores = []

    def update(self, score):
        self.scores.append(score)

        if len(self.scores) < self.ltg:
            self.scores = sorted(self.scores, reverse=True)
        else:
            self.scores = sorted(self.scores, reverse=True)[:self.ltg]

    def reset(self):
        self.scores = []
