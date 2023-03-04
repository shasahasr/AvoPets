import flet as ft

def profile(page: ft.Page):
    return ft.View(
        '/profile',
        [
            ft.ElevatedButton(
                'Home', on_click=lambda _: page.go('/home')),
            ft.CircleAvatar(content=ft.Icon(ft.icons.ACCOUNT_CIRCLE_ROUNDED),),
        ]
    )