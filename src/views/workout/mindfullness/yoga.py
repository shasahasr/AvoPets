import flet as ft


def yoga(page: ft.Page):
    return ft.View(
        '/breathing',
        [
            ft.AppBar(title=ft.Text('Breathing'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
        ]
    )
