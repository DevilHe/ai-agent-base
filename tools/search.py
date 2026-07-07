import os
import requests


def web_search(query: str, max_results: int = 3) -> str:
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": os.getenv("TAVILY_API_KEY"),
        "query": query,
        "max_results": max_results,
        "search_depth": "basic",  # 免费档用 basic 即可
    }

    try:
        response = requests.post(url, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get("results", []):
            results.append(f"- {item['title']}\n  {item['content']}\n  {item['url']}")

        return "\n".join(results) if results else f"没有找到关于「{query}」的结果"

    except requests.Timeout:
        return "搜索超时，请稍后重试"
    except requests.RequestException as e:
        return f"搜索网络错误：{e}"
