import flet as ft
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current))))
sys.path.append(parent)
from firebase import *

def profile(page: ft.Page):
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
                ft.Text(get_user_by_id(page.client_storage.get("user_id")).get("email") + "'s Account"),
                alignment=ft.alignment.center,
                padding=50,
            ),
            ft.Container(
                ft.TextField(
                    label="Pet Name",
                ),
                alignment=ft.alignment.center,
                padding=50,
            ),
        ]
    )
