"""
Win-Win Iterative Model (WWIM) - Judge Layer
Judge whether iteration converges and reaches steady state
"""

class WinWinJudge:
    def __init__(self):
        self.max_iter = 1000
        self.converge_threshold = 0.001

    def is_converged(self, history_rewards):
        """
        Judge convergence based on reward history
        history_rewards: list of reward
        return: (bool, reason)
        """
        if len(history_rewards) < 10:
            return False, "Not enough history"

        recent = history_rewards[-10:]
        delta = max(recent) - min(recent)

        if delta < self.converge_threshold:
            return True, f"Converged: delta = {delta}"

        return False, f"Not converged: delta = {delta}"

    def check_system_status(self, iter_num, reward):
        """Comprehensive system status judgment"""
        if iter_num > self.max_iter:
            return "stop_max_iter"
        return "running"
