import flet as ft
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current))))
sys.path.append(parent)
from firebase import *

def cardio(page: ft.Page):

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
        xp += int(e1TextControl.value * 2)
        xp += int(e2TextControl.value)
        xp += int(e3TextControl.value)
        xp += int(e4TextControl.value)
        add_xp(page.client_storage.get("user_id"), xp)
        add_endurance(page.client_storage.get("user_id"), int(e1TextControl.value) + int(e2TextControl.value) + int(e3TextControl.value) + int(e4TextControl.value))
        page.go("/")

    dlg = ft.AlertDiolog(
        title=ft.Text("Information about cardio: "),
        content=ft.Text(
        """
        Benefits of cardio:
        Keep excess pounds at bay.
        Increase your stamina, fitness and strength.
        Ward off viral illnesses.
        Reduce your health risks.
        Manage chronic conditions.
        Strengthen your heart.
        Keep your arteries clear.
        Boost your mood.

        Information from: https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/aerobic-exercise/art-20045541
        """
    ))

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    return ft.View(
        '/cardio',
        [
            ft.AppBar(title=ft.Text('Cardio Workout'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Running",
                                color=ft.colors.WHITE),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE1Counter),
                                e1TextControl,
                                ft.Text(" miles",
                                        color=ft.colors.WHITE),
                                ft.ElevatedButton(
                                    "+", on_click=increaseE1Counter),
                            ]
                        ),
                    ],
                ),
                padding=5,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Walking",
                                color=ft.colors.WHITE),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE2Counter),
                                e2TextControl,
                                ft.Text(" minutes",
                                        color=ft.colors.WHITE),
                                ft.ElevatedButton(
                                    "+", on_click=increaseE2Counter),
                            ]
                        ),
                    ],
                ),
                padding=5,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Jump Rope",
                                color=ft.colors.WHITE),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE3Counter),
                                e3TextControl,
                                ft.Text(" minutes",
                                        color=ft.colors.WHITE),
                                ft.ElevatedButton(
                                    "+", on_click=increaseE3Counter),
                            ]
                        ),
                    ]
                ),
                padding=5,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Biking",
                                color=ft.colors.WHITE),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE4Counter),
                                e4TextControl,
                                ft.Text(" miles",
                                        color=ft.colors.WHITE),
                                ft.ElevatedButton(
                                    "+", on_click=increaseE4Counter),
                            ]
                        ),
                    ],
                ),
                padding=5,
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content = ft.Row([ft.ElevatedButton("Finish Workout", on_click = finishWorkout), ft.ElevatedButton("More Info", on_click=open_dlg)])
            ),
        ]
    )
