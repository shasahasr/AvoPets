from firebase import *
from time import sleep
import flet as ft
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(current))))
sys.path.append(parent)


def meditation(page: ft.Page):

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

    def finishWorkout(e):
        xp = 0
        if int(e1TextControl.value) > 0 and int(e1TextControl.value) > 0 and int(e1TextControl.value) > 0 and int(e1TextControl.value) > 0:
            xp += 50
        xp += int(e1TextControl.value)
        xp += int(e2TextControl.value)
        xp += int(e3TextControl.value)
        xp += int(e4TextControl.value)
        add_xp(page.client_storage.get("user_id"), xp)
        add_health(page.client_storage.get("user_id"), int(e1TextControl.value) +
                   int(e2TextControl.value) + int(e3TextControl.value) + int(e4TextControl.value))
        page.go("/")

    return ft.View(
        '/meditation',
        [
            ft.AppBar(title=ft.Text('Meditation'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text(
                "Insturctions for Meditating. Warning: This takes time to master, but if you continue you can do it :)"),
            ft.Text("""1) Take a seat
                    Find place to sit that feels calm and quiet to you.

                    2) Set a time limit
                    If you’re just beginning, it can help to choose a short time, such as five or 10 minutes.

                    3) Notice your body
                    You can sit in a chair with your feet on the floor, you can sit loosely cross-legged, you can kneel—all are fine. Just make sure you are stable and in a position you can stay in for a while.

                    4) Feel your breath
                    Follow the sensation of your breath as it goes in and as it goes out.

                    5) Notice when your mind has wandered
                    Inevitably, your attention will leave the breath and wander to other places. When you get around to noticing that your mind has wandered—in a few seconds, a minute, five minutes—simply return your attention to the breath.

                    6) Be kind to your wandering mind
                    Don’t judge yourself or obsess over the content of the thoughts you find yourself lost in. Just come back.

                    7) Close with kindness
                    When you’re ready, gently lift your gaze (if your eyes are closed, open them). Take a moment and notice any sounds in the environment. Notice how your body feels right now. Notice your thoughts and emotions.

            """),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Time Meditated: ",
                                color=ft.colors.WHITE),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "-", on_click=decreaseE1Counter),
                                e1TextControl,
                                ft.Text(" minutes",
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
                content=ft.ElevatedButton(
                    "Finish Meditating", on_click=finishWorkout)
            ),
        ]
    )
