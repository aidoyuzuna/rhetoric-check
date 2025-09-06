from anthropic import Anthropic
from dotenv import load_dotenv
from openai import OpenAI
import os


class AIService:
    """AI APIの処理を管理するクラス"""

    def __init__(self):
        """APIクライアントを初期化"""
        load_dotenv()
        self.chatgpt = OpenAI(api_key=os.environ.get("OPENAI_KEY"))
        self.claude = Anthropic(api_key=os.environ.get("ANTHROPIC_KEY"))

    def get_responses(self, question: str) -> tuple[str | None, str]:
        """ChatGPT・Claudeに質問を投げ、返答を返す

        Args:
            question (str): 質問内容
            selected_model_option (str): ChatGPT・Claudeのモデル設定

        Returns:
            tuple[str | None, str]: ChatGPT・Claudeの返答
        """
        # 各種モデルに回答を出してもらう
        chatgpt_response_message = self.chatgpt.responses.create(
            model="gpt-5",
            input=question,
        )

        claude_response_message = self.claude.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=5000,
            messages=[{"role": "user", "content": question}],
        )

        return (
            chatgpt_response_message.output_text,
            claude_response_message.content[0].text,
        )
