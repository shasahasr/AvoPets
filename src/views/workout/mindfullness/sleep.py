import flet as ft


def sleep(page: ft.Page):
    return ft.View(
        '/sleep',
        [
            ft.AppBar(title=ft.Text('Sleep'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text("Sleep Good pls"),
            ft.Text("How many hours did you sleep last night?"),
            ft.Slider(min=0, max=15, divisions=1, value=8, label="{value}")
        ]
    )
