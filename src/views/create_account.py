import flet as ft

def create_account(page: ft.Page):
    def upchange():
        print("UPUP")

    return ft.View(
        '/create_account',
        [
            ft.Text("Create an Account"),
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
                ft.FilledButton(text="Create Your Account"),
                alignment=ft.alignment.center,
                padding=50,
            ),
        ]
    )