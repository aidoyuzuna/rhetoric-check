from ai_service import AIService
import flet as ft
import winsound


class AppController:
    """アプリケーションの制御を管理するクラス"""

    def __init__(self, page: ft.Page, input_box, chatgpt_response, claude_response):
        """コントローラーを初期化

        Args:
            page (ft.Page): Fletのページオブジェクト
            input_box: 入力テキストボックス
            chatgpt_response: ChatGPT回答エリア
            claude_response: Claude回答エリア
        """
        self.page = page
        self.ai_service = AIService()
        self.input_box = input_box
        self.chatgpt_response = chatgpt_response
        self.claude_response = claude_response
        self.submit_button = None
        self.clear_button = None

    def set_buttons(self, submit_button, clear_button):
        """ボタンの参照を設定

        Args:
            submit_button: 送信ボタン
            clear_button: クリアボタン
        """
        self.submit_button = submit_button
        self.clear_button = clear_button

    def on_keyboard(self, k: ft.KeyboardEvent):
        """キーボードを押したときの挙動を設定

        Args:
            k (ft.KeyboardEvent): キーボードの入力キー
        """
        if k.key == "F" and k.ctrl:
            self.input_box.focus()

        if k.key == "R" and k.ctrl:
            self.on_clear_click("")

        if k.key == "Enter" and k.ctrl:
            self.send_click("")

    def send_click(self, e):
        """テキストエリア送信

        Args:
            e: イベントオブジェクト
        """
        # 回答中の処理を行う
        self.submit_button.disabled = True
        self.clear_button.disabled = True

        self.chatgpt_response.value = "回答中"
        self.claude_response.value = "回答中"
        self.page.update()

        # 返答・表示処理

        send_text = f"以下の投稿から「論理破綻・詭弁・認知のゆがみ」を見つけてください。/n投稿内容：{self.input_box.value}"

        chatgpt_result, claude_result = self.ai_service.get_responses(send_text)

        self.chatgpt_response.value = chatgpt_result
        self.claude_response.value = claude_result

        self.submit_button.disabled = False
        self.clear_button.disabled = False
        self.page.update()
        winsound.PlaySound("fin.wav", winsound.SND_FILENAME)

    def on_clear_click(self, e):
        """テキストエリアリセット

        Args:
            e: イベントオブジェクト
        """
        self.input_box.value = ""
        self.chatgpt_response.value = ""
        self.claude_response.value = ""
        self.input_box.update()
        self.chatgpt_response.update()
        self.claude_response.update()

    def _disable_buttons(self):
        """ボタンを無効化"""
        self.submit_button.disabled = True
        self.clear_button.disabled = True
        self.page.update()

    def _enable_buttons(self):
        """ボタンを有効化"""
        self.submit_button.disabled = False
        self.clear_button.disabled = False
        self.page.update()
