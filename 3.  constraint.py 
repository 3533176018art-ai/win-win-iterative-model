"""
Win-Win Iterative Model (WWIM) - Constraint Layer
Responsible for value constraints, security red lines, and logical stability
"""

class WinWinConstraint:
    def __init__(self):
        # Basic compliance red lines
        self.red_lines = [
            "no_harm",
            "no_illegal",
            "no_pollution",
            "logical_stability"
        ]

    def check_constraint(self, action, reward):
        """
        Check if the action and reward comply with win-win constraints
        return: (is_legal, message)
        """
        is_legal = True
        message = "Constraint check pass"

        # Extensible: value check, security check, gradient check
        if reward < 0:
            is_legal = False
            message = "Negative reward violates win-win principle"

        return is_legal, message
