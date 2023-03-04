import flet as ft


def home(page: ft.Page):
<<<<<<< Updated upstream
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
=======
    if page.client_storage.contains_key("user_id"):
        return ft.View(
            "/",
            [
                ft.ElevatedButton('Login', on_click= lambda _: page.go('/logout')),
                ft.Row([
                    ft.Column([
                        ft.Text("Stats", size=20),
                        ft.Text("Strength: "),
                        ft.Text("Endurance: "),
                    ]),
                    ft.Text("Avocado Goes Here", size = 50),
                ])
            ]
        )
    else:
        return ft.View(
            "/",
            [
                ft.Text("Join or Create an Account"),
                ft.Row([
                    ft.ElevatedButton('Login', on_click= lambda _: page.go('/login')),
                    ft.ElevatedButton('Create an Account', on_click= lambda _: page.go('/create_account')),
                ])
            ]
        )
>>>>>>> Stashed changes
