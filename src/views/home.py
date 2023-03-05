from firebase import *
import flet as ft
from math import floor
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def home(page: ft.Page):

    if page.client_storage.contains_key("user_id"):
        user = get_user_by_id(page.client_storage.get("user_id"))
        pb = ft.ProgressBar(width=400)
        pb.value = ((user.get("pet")["currentxp"]) /
                    (user.get("pet")["neededxp"]))
        page.update()

        return ft.View(
            "/",
            [
                ft.Row([
                    ft.Container(
                        content=ft.Column([
                            ft.Container(
                                ft.Text(user.get("pet")[
                                    "name"] + "'s Stats", size=40),
                                alignment=ft.alignment.top_center,
                                padding=ft.padding.only(top=(page.height/8)*2)
                            ),
                            ft.Container(
                                ft.Text("Health: " + str(floor(user.get("pet")["health"])), size=30), alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                ft.Text("Strength: " +
                                        str(floor(user.get("pet")["strength"])), size=30),
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                ft.Text("Endurance: " +
                                        str(floor(user.get("pet")["endurance"])), size=30),
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                ft.Text("XP Level " +
                                        str(user.get("pet")["currentlevel"]), size=30),
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                ft.Text("XP Progress", style="headlineSmall"),
                                alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                ft.Column([pb]),
                                alignment=ft.alignment.center,
                                padding=ft.padding.only(
                                    bottom=(page.height/8)*2)
                            ),
                        ]),
                        width=page.width/2,
                        height=(page.height/8) * 7,
                    ),
                    ft.Container(
                        content=ft.Image(
                            src=f"./assets/idle0.gif",
                            width=(page.height/8) * 7,
                            height=(page.height/8) * 7,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                        alignment=ft.alignment.center
                    ),
                ]),
                ft.Row([
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(
                                    ft.icons.ACCOUNT_CIRCLE_ROUNDED),
                                ft.Text("Profile"),
                            ]
                        ),
                        on_click=lambda _: page.go('/profile'),
                        height=page.height/8,
                        width=page.width/4,
                        alignment=ft.alignment.top_center,

                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.ARROW_UPWARD_ROUNDED),
                                ft.Text("Train"),
                            ]
                        ),
                        on_click=lambda _: page.go('/train'),
                        height=page.height/8,
                        width=page.width/4,
                        alignment=ft.alignment.top_center,

                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.FLAG_ROUNDED),
                                ft.Text("Battle"),
                            ]
                        ),
                        on_click=lambda _: page.go('/battle'),
                        height=page.height/8,
                        width=page.width/4,
                        alignment=ft.alignment.top_center,
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.EXIT_TO_APP_ROUNDED),
                                ft.Text("Logout"),
                            ]
                        ),
                        on_click=lambda _: page.go('/logout'),
                        height=page.height/8,
                        width=page.width/4,
                        alignment=ft.alignment.top_center,

                    ),
                ],
                ),
            ],
        )
    else:
        return ft.View(
            "/",
            [
                ft.Container(
                    content=ft.Row([
                        ft.Column([
                            ft.Container(
                                ft.Text("AvoPets", size=60, color="#5dc447"),
                                alignment=ft.alignment.top_left,
                            ),
                            ft.Container(
                                ft.Text("Log In or Create an Account"),
                                alignment=ft.alignment.top_left,
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    'Log In', on_click=lambda _: page.go('/login')),
                                alignment=ft.alignment.top_left,
                            ),
                            ft.Container(
                                ft.ElevatedButton(
                                    'Create an Account', on_click=lambda _: page.go('/create_account')),
                                alignment=ft.alignment.top_left,
                            ),
                        ]),
                        ft.Container(
                            content=ft.Image(
                                src=f"./assets/title_screen.gif",
                                width=900,
                                height=900,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            alignment=ft.alignment.center_right
                        ),
                    ]),
                    alignment=ft.alignment.center,
                )
            ]
        )
