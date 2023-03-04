import flet as ft


def pull(page: ft.Page):

    return ft.View(
        '/pull',
        [
            ft.AppBar(title=ft.Text('Pull Workout'),
                      bgcolor=ft.colors.SURFACE_VARIANT)
            
        ]
    )
