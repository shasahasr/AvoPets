import flet as ft
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from firebase import *

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
                            ft.Text(user.get("pet")["name"] + "'s Stats", size=20),
                            ft.Text("Health: " + str(user.get("pet")["health"])),
                            ft.Text("Strength: " + str(user.get("pet")["strength"])),
                            ft.Text("Endurance: " + str(user.get("pet")["endurance"])),
                            ft.Row([
                                ft.Text("XP Level " + str(user.get("pet")["currentlevel"])),
                                ft.Text(str(user.get("pet")["currentxp"]) + "/" + str(user.get("pet")["neededxp"]))
                            ])
                        ]),
                        ft.Text("Avocado Goes Here", size=50),
                    ],
                    alignment=ft.alignment.center
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
                ft.Text("Join or Create an Account"),
                ft.Row([
                    ft.ElevatedButton(
                        'Login', on_click=lambda _: page.go('/login')),
                    ft.ElevatedButton(
                        'Create an Account', on_click=lambda _: page.go('/create_account')),
                    ft.ElevatedButton(
                        'Profile', on_click=lambda _: page.go('/profile')),
                ])
            ]
        )
