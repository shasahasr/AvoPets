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

        return ft.View(
            "/",
            [
                ft.ElevatedButton(
                    'Logout', on_click=lambda _: page.go('/logout')),
                ft.Row(
                    [
                        ft.Column([
                            ft.Text(user.get("pet")[
                                    "name"] + "'s Stats", size=20),
                            ft.Text("Health: " +
                                    str(user.get("pet")["health"])),
                            ft.Text("Strength: " +
                                    str(user.get("pet")["strength"])),
                            ft.Text("Endurance: " +
                                    str(user.get("pet")["endurance"])),
                            ft.Row([
                                ft.Text("XP Level " +
                                        str(user.get("pet")["currentlevel"])),
                                ft.Text(
                                    str(user.get("pet")["currentxp"]) + "/" + str(user.get("pet")["neededxp"]))
                            ])
                        ]),
                    ],
                    alignment=ft.alignment.center,
                ),
                ft.Row([
                    ft.Container(content=ft.ElevatedButton(
                        'Train',
                        on_click=lambda _: page.go('/train'),
                    ), alignment=ft.alignment.bottom_left),
                    ft.Container(content=ft.ElevatedButton(
                        'Battle',
                        on_click=lambda _: page.go('/battle'),
                    ), alignment=ft.alignment.bottom_center),
                    ft.Container(content=ft.ElevatedButton(
                        'Profile',
                        on_click=lambda _: page.go('/profile'),
                    ), alignment=ft.alignment.bottom_right),
                ]),
            ]
        )
    else:
        return ft.View(
            "/",
            [
                ft.Container(
                    ft.Text("AvoPets", size=60),
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
            ]
        )
