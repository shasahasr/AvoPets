import flet as ft


def home(page: ft.Page):
    return ft.View(
        "/",
        [
            ft.ElevatedButton('Login', on_click= lambda _: page.go('/login')),
            ft.ElevatedButton('Create an Account', on_click= lambda _: page.go('/create_account')),
            ft.Row([
                ft.Column([
                    ft.Text("Stats", size=20),
                    ft.Text("Strength: "),
                    ft.Text("Endurance: "),
                ]),
                ft.Text("Avacado Goes Here", size = 50),
            ])
        ]
    )
