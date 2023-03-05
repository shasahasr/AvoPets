import flet as ft


def profile(page: ft.Page):
    return ft.View(
        '/profile',
        [
            ft.AppBar(title=ft.Text('Profile'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Container(
                ft.CircleAvatar(content=ft.Icon(
                    ft.icons.ACCOUNT_CIRCLE_ROUNDED, size=180), radius=100),
                alignment=ft.alignment.center,
            ),
            ft.Column(
                
            )
        ]
    )
