from firebase import *
import flet as ft
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
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.icons.ACCOUNT_CIRCLE_ROUNDED),
                                    ft.Text("Profile"),
                                ]
                            ),
                            on_click=lambda _: page.go('/profile'),
                        ),
                        ft.PopupMenuItem(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.icons.ARROW_UPWARD_ROUNDED),
                                    ft.Text("Train"),
                                ]
                            ),
                            on_click=lambda _: page.go('/train'),
                        ),
                        ft.PopupMenuItem(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.icons.FLAG_ROUNDED),
                                    ft.Text("Battle"),
                                ]
                            ),
                            on_click=lambda _: page.go('/battle'),
                        ),
                        ft.PopupMenuItem(
                            content=ft.Row(
                                [
                                    ft.Icon(ft.icons.EXIT_TO_APP_ROUNDED),
                                    ft.Text("Logout"),
                                ]
                            ),
                            on_click=lambda _: page.go('/logout'),
                        ),
                    ],
                    icon=ft.icons.MENU_ROUNDED,
                ),
                ft.Container(
                    ft.Text(user.get("pet")[
                        "name"] + "'s Stats", size=20),
                    alignment=ft.alignment.top_center,
                ),
                ft.Container(
                    ft.Text("Health: " +
                            str(user.get("pet")["health"])),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text("Strength: " +
                            str(user.get("pet")["strength"])),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text("Endurance: " +
                            str(user.get("pet")["endurance"])),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text("XP Level " +
                            str(user.get("pet")["currentlevel"])),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text("XP Progress", style="headlineSmall"),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Column([pb]),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    content=ft.Image(
                        src=f"./assets/idle0.png",
                        width=600,
                        height=600,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center
                )
            ]
        )
    else:
        return ft.View(
            "/",
            [
                ft.Container(
                    ft.Text("AvoPets", size=60, color="#5dc447"),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.Text("Join or Create an Account"),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.ElevatedButton(
                        'Login', on_click=lambda _: page.go('/login')),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    ft.ElevatedButton(
                        'Create an Account', on_click=lambda _: page.go('/create_account')),
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    content=ft.Image(
                        src=f"./assets/idle0.png",
                        width=600,
                        height=600,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center
                )
            ]
        )
