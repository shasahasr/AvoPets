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
                ft.Container(
                    ft.Text(user.get("pet")[
                        "name"] + "'s Stats", size=20),
                    alignment=ft.alignment.center,
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
                    ft.Row([
                        ft.Text("XP Level " +
                                str(user.get("pet")["currentlevel"])),
                        ft.Text(
                            str(user.get("pet")["currentxp"]) + "/" + str(user.get("pet")["neededxp"]))
                    ]),
                    alignment=ft.alignment.center,
                ),
                ft.Row([
                    ft.Container(ft.ElevatedButton(
                        'Train',
                        on_click=lambda _: page.go('/train'),
                    ), alignment=ft.alignment.bottom_center),
                    ft.Container(ft.ElevatedButton(
                        'Battle',
                        on_click=lambda _: page.go('/battle'),
                    ), alignment=ft.alignment.bottom_center),
                    ft.Container(ft.ElevatedButton(
                        'Profile',
                        on_click=lambda _: page.go('/profile'),
                    ), alignment=ft.alignment.bottom_center),
                ]),
            ]
        )
    else:
        return ft.View(
            "/",
            [
                ft.Container(
                    ft.Text("AvoPets", size=60, color="#5a954a"),
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
