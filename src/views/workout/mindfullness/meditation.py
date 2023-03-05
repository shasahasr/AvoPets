from time import sleep
import flet as ft


def meditation(page: ft.Page):
    return ft.View(
        '/meditation',
        [
            ft.AppBar(title=ft.Text('Meditation'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
        ]
    )
