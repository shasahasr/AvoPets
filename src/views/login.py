import flet as ft

def login(page: ft.Page):
    def upchange():
        print("UPUP")

    return ft.View(
        '/login',
        [
            ft.Container(
                ft.TextField(label="Username"),
                alignment=ft.alignment.center,
                padding=50,
            ),
            ft.Container(
                ft.TextField(label="Password", password = True, can_reveal_password=True),
                alignment=ft.alignment.center,
                padding=50,
            ),
            ft.Container(
                ft.FilledButton(text="Login"),
                alignment=ft.alignment.center,
                padding=50,
            ),
        ]
    )