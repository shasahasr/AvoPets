import flet as ft

def battle(page: ft.Page):
    return ft.View(
        "/battle",
        [
            ft.AppBar(title=ft.Text('Battle'), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text("battle lmfao")
        ]
    )