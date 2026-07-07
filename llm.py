import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)


def chat(messages: list[dict]) -> str:
    """
    发送消息列表给 AI，返回 AI 的回复文字。

    messages 格式：
    [
      {"role": "system", "content": "你是一个AI智能助手，请根据用户的问题给出回答。"},
      {"role": "user",   "content": "你好"},
    ]
    """
    response = client.chat.completions.create(
        model="agnes-2.0-flash",  # API 改成对应模型名
        messages=messages,
        temperature=0,  # 温度，0 = 输出更稳定；1 = 输出更随机
    )
    return response.choices[0].message.content
