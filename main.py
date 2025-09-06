import flet as ft
from flet import margin
from app_controller import AppController
from components import MyField, MyButton, AnswerField


def main(page: ft.Page):
    # ページの設定
    page.title = "論理チェックアプリ"
    page.window.width = 1200
    page.window.height = 900

    # 悩み・質問を書くテキストボックス
    input_box = MyField("気になる文章を書く")

    # 回答エリア
    chatgpt_response = AnswerField(
        label="ChatGPTの回答",
    )
    claude_response = AnswerField(
        label="Claudeの回答",
    )

    # コントローラーのインスタンスを作成（UIコンポーネントを渡す）
    controller = AppController(page, input_box, chatgpt_response, claude_response)

    # 送信、コピー、リセットボタンの設定
    submit_button = MyButton(
        text="送信",
        width=300,
        bgcolor="#F44336",
        color="#ffffff",
        disabled=False,
        on_click=controller.send_click,
    )

    clear_button = MyButton(
        text="リセット",
        width=200,
        bgcolor="#757575",
        color="#ffffff",
        disabled=False,
        on_click=controller.on_clear_click,
    )

    # ボタンの参照をコントローラーに設定
    controller.set_buttons(submit_button, clear_button)

    # キーボードイベントを設定
    page.on_keyboard_event = controller.on_keyboard

    # レイアウトの作成
    page.add(
        ft.Container(input_box, margin=margin.only(bottom=10, left=75)),
        ft.Container(
            ft.Row(
                [submit_button, clear_button],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            margin=margin.only(bottom=30),
        ),
        ft.Container(
            ft.Row(
                [chatgpt_response, claude_response],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ),
    )


# アプリケーションの開始
if __name__ == "__main__":
    ft.app(target=main)
