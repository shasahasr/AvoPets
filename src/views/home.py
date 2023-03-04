import flet as ft

def home(page: ft.Page):
    return ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.ElevatedButton('Go to Login', on_click=lambda _: page.go('/login'))
        ]
    )