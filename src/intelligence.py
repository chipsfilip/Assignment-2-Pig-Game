# computer player that plays automatically (AI)
class Intelligence:

    # computer holds if points >= 20
    def computer_hold(self, turn_score):
        if turn_score >= 20:
            return True
        else:
            return False
