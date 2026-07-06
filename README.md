# 从零开始搭建第一个基础版 AI Agent

不用 LangChain，不用 AutoGen，从最小 Agent 开始，一步步开始搭建一个基础版 AI Agent。

---

## 最终效果

运行 `main.py` 后，你会得到一个支持多工具、有记忆、能多步推理的 Agent：

```
=================================================
    我的 AI Agent 系统 v1.0
=================================================
命令：
  直接输入    → 对话模式（有记忆，自动使用工具）
  /plan <任务> → 规划模式（先制定计划再执行）
  /clear      → 清除对话记忆
  /quit       → 退出
=================================================

你：帮我搜索一下最近 AI 领域的新闻

[步骤 1/5]
[AI 思考]: {"type": "tool_call", "tool": "web_search", ...}
[调用工具]: web_search
[工具结果]: ...

Agent：根据最新搜索结果，以下是 AI 领域近期重要动态：...
```

---

## 快速开始（5 分钟内跑通）

### 第一步：下载代码

```bash
git clone https://github.com/你的用户名/ai-agent-base.git
cd ai-agent-base
```

### 第二步：安装依赖

```bash
# 创建虚拟环境
python -m venv .venv
# 激活虚拟环境
source .venv/bin/activate
# 安装依赖
pip install -r requirements.txt
```

> 需要 Python 3.10 或以上版本。检查版本：`python --version`

### 第三步：配置 API Key

```bash
cp .env.example .env
```

用文本编辑器打开 `.env`，把 `sk-xxx` 替换成你的真实 Key。

### 第四步：运行第一个 Agent

```bash
python main.py
```

看到 `=== 我的第一个 Agent ===` 就成功了。

---

## 需要什么基础

- Python 基础（变量、函数、if/else、for 循环）
- 一个 OpenAI API Key，或者任何兼容 OpenAI 格式的服务
- 暂不需要 LangChain / AutoGen / 任何 Agent 框架

---

## API Key 去哪里拿

**OpenAI 官方（推荐，效果最好）：**

- 注册：https://platform.openai.com
- 价格：gpt-4o-mini 非常便宜，跑完 7 天课程大约花 $0.5 以内

**国内替代方案（不需要梯子）：**

- DeepSeek：https://platform.deepseek.com（效果接近 GPT-4，价格极低）
- 月之暗面：https://platform.moonshot.cn
- 智谱 AI：https://open.bigmodel.cn

**如何切换到国内 API：**

修改目录里的 `llm.py`：

```python
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url="https://api.deepseek.com",  # 改这里
)

# chat 函数里的 model 也要改：
model="deepseek-chat"
```

在 `.env` 里填入对应平台的 Key 即可，其他代码不用动。

---

## 项目结构

```
my-first-agent/
├── examples/        # 示例
├── main.py
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## 学完之后能做什么

通过本项目，你会真正理解 Agent 的工作原理，而不是只会用框架。

之后可以继续探索：

- 换成 LangChain / LlamaIndex（你会发现它们解决的正是你亲手遇到的问题）
- 给 Agent 加上更多工具（发邮件、操作文件、调用数据库）
- 做一个有 Web 界面的 Agent（用 FastAPI + 简单前端）
- 探索 Multi-Agent 系统（多个 Agent 协作）
