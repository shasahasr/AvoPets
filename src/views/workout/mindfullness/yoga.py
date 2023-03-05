import flet as ft


def yoga(page: ft.Page):
    return ft.View(
        '/yoga',
        [
            ft.AppBar(title=ft.Text('Yoga'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
        ]
    )
