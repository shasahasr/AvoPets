from firebase import *
import flet as ft
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(current))))
sys.path.append(parent)

pet_name = ""


def profile(page: ft.Page):
    def change_pet_name(e):
        global pet_name

        pet_name = e.control.value

    def change_p_name(e):
        global pet_name

        change_name(page.client_storage.get("user_id"), pet_name)
        page.update()

    return ft.View(
        '/profile',
        [
            ft.AppBar(title=ft.Text('Profile'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Container(
                ft.CircleAvatar(content=ft.Icon(
                    ft.icons.ACCOUNT_CIRCLE_ROUNDED, size=180), radius=100),
                alignment=ft.alignment.center,
            ),
            ft.Container(
                ft.Text(get_user_by_id(page.client_storage.get(
                    "user_id")).get("email") + "'s Account"),
                alignment=ft.alignment.center,
                padding=50,
            ),
            ft.Container(
                ft.TextField(
                    label="Pet Name",
                    on_change=change_pet_name,
                ),
                alignment=ft.alignment.center,
                padding=50,
            ),
            ft.Container(
                ft.ElevatedButton("Change Pet Name", on_click=change_p_name),
                alignment=ft.alignment.center,
            ),

        ]
    )
