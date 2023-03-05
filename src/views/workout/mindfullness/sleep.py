import flet as ft


def sleep(page: ft.Page):
    return ft.View(
        '/sleep',
        [
            ft.AppBar(title=ft.Text('Sleep'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Image(
                src=f"./assets/fork0.gif",
                width=700,
                height=700,
                fit=ft.ImageFit.CONTAIN,
            )
        ]
    )
