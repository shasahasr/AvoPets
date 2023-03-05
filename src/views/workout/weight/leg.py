import flet as ft
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current))))
sys.path.append(parent)
from firebase import *

def leg(page: ft.Page):

    e1TextControl = ft.Text(value="0",
                            color=ft.colors.WHITE)

    e2TextControl = ft.Text(value="0",
                            color=ft.colors.WHITE)

    e3TextControl = ft.Text(value="0",
                            color=ft.colors.WHITE)

    e4TextControl = ft.Text(value="0",
                            color=ft.colors.WHITE)

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
        
    def finishWorkout(e):
        xp = 0
        if int(e1TextControl.value) > 0 and int(e1TextControl.value) > 0 and int(e1TextControl.value) > 0 and int(e1TextControl.value) > 0:
            xp += 50
        xp += int(e1TextControl.value)
        xp += int(e2TextControl.value)
        xp += int(e3TextControl.value)
        xp += int(e4TextControl.value)
        add_xp(page.client_storage.get("user_id"), xp)
        add_strength(page.client_storage.get("user_id"), int(e1TextControl.value) + int(e2TextControl.value) + int(e3TextControl.value) + int(e4TextControl.value))
        page.go("/")

    def finishWorkout(e):
        xp = 0
        if int(e1TextControl.value) > 0 and int(e1TextControl.value) > 0 and int(e1TextControl.value) > 0 and int(e1TextControl.value) > 0:
            xp += 50
        xp += int(e1TextControl.value)
        xp += int(e2TextControl.value)
        xp += int(e3TextControl.value)
        xp += int(e4TextControl.value)
        add_xp(page.client_storage.get("user_id"), xp)
        add_strength(page.client_storage.get("user_id"), int(e1TextControl.value) + int(e2TextControl.value) + int(e3TextControl.value) + int(e4TextControl.value))
        page.go("/")

    return ft.View(
        '/leg',
        [
            ft.AppBar(title=ft.Text('Leg'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Squats",
                                color=ft.colors.WHITE, size=50),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE1Counter),
                                e1TextControl,
                                ft.Text(" reps",
                                        color=ft.colors.WHITE, size=30),
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
                        ft.Text("Lunges",
                                color=ft.colors.WHITE, size=50),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE2Counter),
                                e2TextControl,
                                ft.Text(" reps",
                                        color=ft.colors.WHITE, size=30),
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
                        ft.Text("Calf Raises",
                                color=ft.colors.WHITE, size=50),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE3Counter),
                                e3TextControl,
                                ft.Text(" reps",
                                        color=ft.colors.WHITE, size=30),
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
                        ft.Text("Stairs",
                                color=ft.colors.WHITE, size=50),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE4Counter),
                                e4TextControl,
                                ft.Text(" flights",
                                        color=ft.colors.WHITE, size=30),
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
            ft.Container(
                content = ft.ElevatedButton("Finish Workout", on_click = finishWorkout)
            )
        ]
    )
