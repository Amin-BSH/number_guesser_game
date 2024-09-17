class Scorer:
    """Scorer class maintain the score board of the game"""

    def __init__(self, score: int = 100) -> None:
        self.score = 100

    def decrement_score(self):
        """decrease the score of the player"""
        self.score -= 10
        self.score = max(self.score, 0)

    def return_score(self):
        return self.score


if __name__ == "__main__":
    scorer = Scorer()
    scorer.decrement_score()
    print(scorer.return_score())
