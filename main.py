import flet as ft

def main(page: ft.Page):
    page.title = "测试"
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("测试", theme_style=ft.TextThemeStyle.TITLE_LARGE),
                    ]
                ),
                width=400,
                height=500,
            )
        )
    )

ft.app(main)