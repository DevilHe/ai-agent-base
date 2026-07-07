import os
import json
import httpx


def get_weather(city: str) -> str:
    """
    查询即时天气函数
    :param city: 城市英文名，如 Beijing、Shanghai。
    :return: OpenWeather API 返回的天气信息（JSON 字符串）。
    """

    url = os.getenv("OPENWEATHER_API_URL")
    params = {
        "q": city,
        "appid": os.getenv("OPENWEATHER_API_KEY"),
        "units": "metric",
        "lang": "zh_cn",
    }
    response = httpx.get(url, params=params, timeout=30)
    data = response.json()
    return json.dumps(data, ensure_ascii=False)
