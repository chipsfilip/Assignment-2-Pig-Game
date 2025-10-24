class Computer:
    """Computer player that plays automatically (AI)"""
    def intelligence(self, turn_score):
        """Computer holds if points is greater than 20"""
        if turn_score >= 20:
            return True
        else:
            return False
