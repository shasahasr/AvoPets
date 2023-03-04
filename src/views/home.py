import flet as ft


def home(page: ft.Page):
    if page.client_storage.contains_key("user_id"):
        return ft.View(
            "/",
            [
                ft.ElevatedButton(
                    'Login', on_click=lambda _: page.go('/logout')),
                ft.Row([
                    ft.Column([
                        ft.Text("Stats", size=20),
                        ft.Text("Strength: "),
                        ft.Text("Endurance: "),
                    ]),
                    ft.Text("Avocado Goes Here", size=50),
                    ft.ElevatedButton('Train',
                                      on_click=lambda _: page.go('/train')),
                ])
            ]
        )
    else:
        return ft.View(
            "/",
            [
                ft.Text("Join or Create an Account"),
                ft.Row([
                    ft.ElevatedButton(
                        'Login', on_click=lambda _: page.go('/login')),
                    ft.ElevatedButton(
                        'Create an Account', on_click=lambda _: page.go('/create_account')),
                ])
            ]
        )
