import json
import re
from tools.weather import get_weather


def safe_parse_json(text: str) -> dict:
    """从 AI 回复里提取 JSON，即使 AI 多说了废话也能处理。"""
    # 先尝试直接解析
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # 尝试从文本里找 {...} 块
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    # 兜底：把原文当作普通回答
    return {"action": "answer", "content": text}


def execute_action(ai_response: str) -> str:
    """解析 AI 返回的 JSON，执行对应动作。"""
    decision = safe_parse_json(ai_response)
    action = decision.get("action")

    if action == "answer":
        return decision.get("content", "（AI 没有提供内容）")

    elif action == "get_weather":
        city = decision.get("city", "未知城市")
        weather = get_weather(city)
        return f"{city}的天气：{weather}"

    else:
        # AI 返回了不认识的动作，直接把内容输出
        return f"(未知动作 {action!r}){decision}"


"""
用户：今天北京的天气
[AI 决策]: {"action": "get_weather", "city": "Beijing"}
Agent：Beijing的天气：{"coord": {"lon": 116.3972, "lat": 39.9075}, "weather": [{"id": 800, "main": "Clear", "description": "晴", "icon": "01d"}], "base": "stations", "main": {"temp": 34.31, "feels_like": 33.53, "temp_min": 34.31, "temp_max": 34.31, "pressure": 998, "humidity": 29, "sea_level": 998, "grnd_level": 993}, "visibility": 10000, "wind": {"speed": 1.09, "deg": 118, "gust": 1.02}, "clouds": {"all": 9}, "dt": 1783396089, "sys": {"country": "CN", "sunrise": 1783371145, "sunset": 1783424741}, "timezone": 28800, "id": 1816670, "name": "Beijing", "cod": 200}
"""
