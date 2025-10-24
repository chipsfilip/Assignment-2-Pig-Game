# computer player that plays automatically (AI)
class Computer:
    # computer holds if points >= 20
    def intelligence(self, turn_score):
        if turn_score >= 20:
            return True
        else:
            return False
