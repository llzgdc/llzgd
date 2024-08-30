import flet as ft


def main(page: ft.Page):
    page.title = "测试"

    page.theme_mode = "light"
    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    print(ft.CrossAxisAlignment)

    page.appbar = ft.AppBar(
        title=ft.Text("测试", color=ft.colors.WHITE),
        bgcolor=ft.colors.BLACK54,
        center_title=True
    )

    def highlight_link(e):
        e.control.style.color = ft.colors.BLUE
        e.control.update()

    def unhighlight_link(e):
        e.control.style.color = None
        e.control.update()

    def sun_btn_c(e):
        if page.theme_mode == "light":
            page.theme_mode = "dark"
        elif page.theme_mode == "dark":
            page.theme_mode = "light"
        e.control.selected = not e.control.selected
        page.update()

    sun_btn = ft.IconButton(
            icon=ft.icons.WB_SUNNY_ROUNDED,
            selected_icon=ft.icons.SHIELD_MOON,
            icon_color="black400",
            icon_size=65,
            selected=False,
            on_click=sun_btn_c,
            data=0,
        )

    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("测试", theme_style=ft.TextThemeStyle.TITLE_LARGE),
                        ft.Divider(height=1, color="gray"),
                        ft.Text("bbb", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                        ft.Text(
                            disabled=False,
                            spans=[
                                ft.TextSpan(
                                    "Bilibili",
                                    ft.TextStyle(decoration=ft.TextThemeStyle.DISPLAY_MEDIUM),
                                    url="https://space.bilibili.com/2019959464",
                                    on_enter=highlight_link,
                                    on_exit=unhighlight_link,
                                ),
                                ft.TextSpan(
                                    "\nGithub",
                                    ft.TextStyle(decoration=ft.TextThemeStyle.DISPLAY_MEDIUM),
                                    url="https://github.com/llzgdc",
                                    on_enter=highlight_link,
                                    on_exit=unhighlight_link,
                                ),
                            ]
                        )
                    ]
                ),
                width=400,
                height=180,
            )
        ),
        sun_btn
    )

ft.app(target=main)
