"""
最小 Agent 示例
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 创建 OpenAI 客户端
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)

# 初始化历史消息
history_messages = [
    {"role": "system", "content": "你是一个AI智能助手，请根据用户的问题给出回答。"}
]

# 循环获取用户输入
while True:
    # 获取用户输入
    msg = input("用户:")
    history_messages.append({"role": "user", "content": msg})

    # 创建 OpenAI 客户端
    response = client.chat.completions.create(
        model="agnes-2.0-flash", messages=history_messages
    )

    # 打印 AI 回复
    print("AI:", response.choices[0].message.content)
    # 更新历史消息
    history_messages.append(
        {"role": "assistant", "content": response.choices[0].message.content}
    )


"""
运行示例：
用户:我是小明，喜欢看足球比赛
AI: 你好，小明！很高兴认识你。⚽️

足球是一项非常充满激情和团队精神的运动。你最喜欢哪支球队或者哪位球员呢？如果有感兴趣的赛事（比如英超、西甲、欧冠或世界杯），也可以和我聊聊，我可以为你介绍相关的赛程、历史数据或者战术分析。
用户:我是谁？
AI: 你是小明，一位喜欢观看足球比赛的球迷。
用户:你认为今年的世界杯冠军会是哪支球队？
AI: 目前并没有“今年”的世界杯。下一届男足世界杯是 **2026年** 的美加墨世界杯，女足世界杯则是 **2027年** 的巴西世界杯。

不过，如果我们要预测未来的冠军，通常有几支传统强队被视为热门候选：

1.  **法国队**：拥有姆巴佩等顶级球星，阵容深度极佳。
2.  **阿根廷队**：作为2022年的冠军，他们拥有梅西（尽管年龄增长）和年轻的迪马利亚、劳塔罗等核心，经验与实力并存。
3.  **英格兰队**：年轻一代球员（如贝林厄姆、福登、萨卡）正值当打之年，实力强劲。
4.  **巴西队**：传统足球强国，永远拥有制造惊喜的潜力。
5.  **德国队/西班牙队**：近期表现稳定，战术素养极高。

但足球的魅力就在于不可预测性！你觉得哪支球队最有希望夺冠呢？⚽️🏆
"""
