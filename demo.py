"""
Win-Win Iterative Model (WWIM) - 示例运行
轻量级演示，用于验证框架可运行
"""

from iter_engine import WinWinIterativeEngine
from constraint import WinWinConstraint
from judge import WinWinJudge

def demo_simple_iteration():
    engine = WinWinIterativeEngine()
    constraint = WinWinConstraint()
    judge = WinWinJudge()

    history_rewards = []

    print("=== Win-Win Iterative Model - Demo Start ===")

    while not engine.converged:
        iter_num, state, action, reward = engine.run_iteration()
        history_rewards.append(reward)

        # 约束检查
        legal, msg = constraint.check_constraint(action, reward)
        if not legal:
            print(f"Constraint violated: {msg}")
            break

        # 收敛判断
        converged, reason = judge.is_converged(history_rewards)
        if converged:
            engine.converged = True
            print(f"Converged at iter {iter_num}: {reason}")

        # 打印信息
        print(f"Iter {iter_num} | Reward {reward:.4f} | {msg}")

    print("=== Demo Finished ===")

if __name__ == "__main__":
    demo_simple_iteration()
