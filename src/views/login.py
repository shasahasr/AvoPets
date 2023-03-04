import flet as ft

def login(page: ft.Page):
    def upchange():
        print("UPUP")

    return ft.View(
        '/login',
        [
            ft.AppBar(title=ft.Text('Flet Login'), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.ElevatedButton('Go to homepage', on_click=lambda _: page.go('/')),
            ft.ElevatedButton('hi hello', on_click=lambda _: upchange())
        ]
    )