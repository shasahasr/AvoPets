import flet as ft


def meditation(page: ft.Page):
    return ft.View(
        '/breathing',
        [
            ft.AppBar(title=ft.Text('Breathing'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
        ]
    )
