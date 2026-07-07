from agent import Agent


def main() -> None:
    print("=== 智能助手 Agent ===")
    print("命令：/clear 清除记忆 | quit 退出\n")

    agent = Agent()

    while True:
        user_input = input("用户：").strip()

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "/quit"):
            print("再见！")
            break

        if user_input.lower() == "/clear":
            agent.clear()
            print("记忆已清除，开始新对话。\n")
            continue

        result = agent.chat(user_input)
        print(f"Agent：{result}\n")
        print(f"（当前记忆：{agent.memory_count()} 条消息）\n")


if __name__ == "__main__":
    main()
