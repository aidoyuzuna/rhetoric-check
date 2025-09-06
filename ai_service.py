from anthropic import Anthropic
from anthropic import AuthenticationError as AnthropicAuthenticationError
from dotenv import load_dotenv
from openai import OpenAI
from openai import AuthenticationError as OpenAIAuthenticationError
import os
from requests.exceptions import HTTPError, RequestException


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
        # 回答結果（エラー含む）を入れる変数を定義
        chatgpt_result = ""
        claude_result = ""

        # ChatGPTの回答S
        try:
            chatgpt_response_message = self.chatgpt.responses.create(
                model="gpt-5",
                input=question,
            )
            chatgpt_result = chatgpt_response_message.output_text

        except OpenAIAuthenticationError:
            chatgpt_result = "OpenAI API認証に失敗しました。APIキーを確認してください。"

        except HTTPError as e:
            if e.response.status_code == 401:
                print("APIキーが無効です")
                chatgpt_result = "OpenAI APIキーが無効または期限切れです"

            elif e.response.status_code == 403:
                chatgpt_result = "OpenAI API利用権限がありません"

            else:
                print(f"HTTPエラー: {e}")
                chatgpt_result = f"エラーが発生しました: {e}"
        except RequestException:
            chatgpt_result = "通信エラーが発生しました"
        except Exception:
            chatgpt_result = "システムエラーが発生しました"

        # Claudeの回答
        try:
            claude_response_message = self.claude.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=5000,
                messages=[{"role": "user", "content": question}],
            )

            claude_result = claude_response_message.content[0].text

        except AnthropicAuthenticationError:
            claude_result = "Claude API認証に失敗しました。APIキーを確認してください。"

        except HTTPError as e:
            if e.response.status_code == 401:
                claude_result = "Claude APIキーが無効または期限切れです"

            elif e.response.status_code == 403:
                claude_result = "Claude API利用権限がありません"

            else:
                claude_result = f"エラーが発生しました: {e}"
        except RequestException:
            claude_result = "通信エラーが発生しました"
        except Exception:
            claude_result = "システムエラーが発生しました"

        return (chatgpt_result, claude_result)
