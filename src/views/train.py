import flet as ft


def train(page: ft.Page):

    def upchange():
        pass
    return ft.View(
        '/train',
        [
            ft.AppBar(title=ft.Text('Training'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text('Weights Routine'),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text="Push", on_click=lambda _: page.go('/push')),
                    ft.ElevatedButton(
                        text="Pull", on_click=lambda _: page.go('/pull')),
                    ft.ElevatedButton(
                        text="Leg", on_click=lambda _: page.go('/leg')),
                    ft.ElevatedButton(
                        text="Cardio", on_click=lambda _: page.go('/cardio')),
                ]
            ),
            ft.Text('Mindfulness Routine'),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="Breathing",
                                      on_click=lambda _: page.go('/breathing')),
                    ft.ElevatedButton(text="Meditation",
                                      on_click=lambda _: page.go('/meditation')),
                    ft.ElevatedButton(
                        text="Yoga", on_click=lambda _: page.go('/yoga')),
                    ft.ElevatedButton(
                        text="Sleep", on_click=lambda _: page.go('/sleep')),
                ]
            ),

        ]
    )
