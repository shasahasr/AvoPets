import flet as ft


def pull(page: ft.Page):

    e1TextControl = ft.Text(value="0",
                            color=ft.colors.BLACK)

    e2TextControl = ft.Text(value="0",
                            color=ft.colors.BLACK)

    e3TextControl = ft.Text(value="0",
                            color=ft.colors.BLACK)

    e4TextControl = ft.Text(value="0",
                            color=ft.colors.BLACK)

    def decreaseE1Counter(e):

        e1TextControl.value = str(int(e1TextControl.value) - 1)

        page.update()

    def increaseE1Counter(e):

        e1TextControl.value = str(int(e1TextControl.value) + 1)

        page.update()

    def decreaseE2Counter(e):

        e2TextControl.value = str(int(e2TextControl.value) - 1)

        page.update()

    def increaseE2Counter(e):

        e2TextControl.value = str(int(e2TextControl.value) + 1)

        page.update()

    def decreaseE3Counter(e):

        e3TextControl.value = str(int(e3TextControl.value) - 1)

        page.update()

    def increaseE3Counter(e):

        e3TextControl.value = str(int(e3TextControl.value) + 1)

        page.update()

    def decreaseE4Counter(e):

        e4TextControl.value = str(int(e4TextControl.value) - 1)

        page.update()

    def increaseE4Counter(e):

        e4TextControl.value = str(int(e4TextControl.value) + 1)

        page.update()

    return ft.View(
        '/pull',
        [
            ft.AppBar(title=ft.Text('pull Workout'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Pullups",
                                color=ft.colors.BLACK),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE1Counter),
                                e1TextControl,
                                ft.Text(" reps",
                                        color=ft.colors.BLACK),
                                ft.ElevatedButton(
                                    "+", on_click=increaseE1Counter),
                            ]
                        ),
                    ],
                ),
                bgcolor=ft.colors.CYAN,
                padding=5,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Curl your mom",
                                color=ft.colors.BLACK),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE2Counter),
                                e2TextControl,
                                ft.Text(" reps",
                                        color=ft.colors.BLACK),
                                ft.ElevatedButton(
                                    "+", on_click=increaseE2Counter),
                            ]
                        ),
                    ],
                ),
                bgcolor=ft.colors.CYAN,
                padding=5,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Lat Pull Downs",
                                color=ft.colors.BLACK),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE3Counter),
                                e3TextControl,
                                ft.Text(" reps",
                                        color=ft.colors.BLACK),
                                ft.ElevatedButton(
                                    "+", on_click=increaseE3Counter),
                            ]
                        ),
                    ]
                ),
                bgcolor=ft.colors.CYAN,
                padding=5,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Dumbell Rows",
                                color=ft.colors.BLACK),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE4Counter),
                                e4TextControl,
                                ft.Text(" reps",
                                        color=ft.colors.BLACK),
                                ft.ElevatedButton(
                                    "+", on_click=increaseE4Counter),
                            ]
                        ),
                    ],
                ),
                bgcolor=ft.colors.CYAN,
                padding=5,
                alignment=ft.alignment.center,
            ),
        ]
    )
