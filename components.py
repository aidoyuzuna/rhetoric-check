import flet as ft


class MyField(ft.TextField):
    def __init__(self, label):
        super().__init__(
            label=label,
            min_lines=4,
            multiline=True,
            width=1010,
            bgcolor="#333333",
            color="#ffffff",
        )


class MyButton(ft.ElevatedButton):
    def __init__(self, text, width, bgcolor, color, disabled, on_click):
        super().__init__(
            text=text,
            width=width,
            height=50,
            bgcolor=bgcolor,
            color=color,
            disabled=disabled,
            on_click=on_click,
        )


class AnswerField(ft.TextField):
    def __init__(self, label):
        super().__init__(
            label=label,
            value="",
            read_only=True,
            width=500,
            height=700,
            min_lines=23,
            max_lines=23,
            bgcolor="#212121",
            multiline=True,
        )
