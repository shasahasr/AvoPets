import flet as ft


def sleep(page: ft.Page):
    return ft.View(
        '/sleep',
        [
            ft.AppBar(title=ft.Text('Sleep'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
        ]
    )
