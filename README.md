# 共赢迭代模型 Win-Win Iterative Model (WWIM)
一个面向通用智能体的轻量化迭代框架，核心思想：
- 以持续迭代替代静态训练
- 以人机共赢作为价值约束
- 以逻辑稳态保证安全可控

本仓库为基础概念版，用于学术交流、原型验证。

## 结构
- iter_engine.py：基础迭代循环
- constraint.py：简单合规约束
- judge.py：基础收敛判断
- demo.py：简单文本对话示例

## 核心逻辑（伪代码）
while not converged:
state = observe()
action = choose_action(state)
reward = win_win_reward(state, action)
update_model(reward)
