from agent_loop import ReactAgent


def main() -> None:
    print("=== 智能助手 Agent ===")
    print("命令：/clear 清除记忆 | quit 退出\n")

    agent = ReactAgent(max_steps=5)

    while True:
        user_input = input("用户：").strip()

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "/quit"):
            print("再见！")
            break

        result = agent.run(user_input)
        print(f"Agent：{result}\n")


if __name__ == "__main__":
    main()
