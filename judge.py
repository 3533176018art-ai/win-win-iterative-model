"""
Win-Win Iterative Model (WWIM) - 收敛判断层
判断迭代是否收敛、是否达到稳态
"""

class WinWinJudge:
    def __init__(self):
        self.max_iter = 1000
        self.converge_threshold = 0.001

    def is_converged(self, history_rewards):
        """
        根据奖励历史判断是否收敛
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
        """综合系统状态判断"""
        if iter_num > self.max_iter:
            return "stop_max_iter"
        return "running"
