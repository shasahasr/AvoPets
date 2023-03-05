import flet as ft


def sleep(page: ft.Page):
    return ft.View(
        '/sleep',
        [
            ft.AppBar(title=ft.Text('Sleep'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Image(
                src=f"./assets/idle0.png",
                width=100,
                height=100,
                fit=ft.ImageFit.CONTAIN,
            )
        ]
    )
