from agent import run_agent


def main() -> None:
    print("=== 我的第一个 Agent ===")
    print("输入 quit 退出\n")

    while True:
        user_input = input("用户：").strip()

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "/quit"):
            print("再见！")
            break

        result = run_agent(user_input)
        print(f"Agent：{result}\n")


if __name__ == "__main__":
    main()
