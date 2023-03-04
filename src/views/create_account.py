import flet as ft

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from firebase import *

usr = ""
password = ""
def create_account(page: ft.Page):
    if page.client_storage.contains_key("user_id"):
        page.go("/")

    def verifyregister(e):
        global usr
        global password
        user = register(usr, password)
        if user:
            page.client_storage.set("user_id", user)
            page.go("/")

    def usernameval(e):
        global usr
        usr = e.control.value

    def passwordval(e):
        global password
        password = e.control.value

    return ft.View(
        '/create_account',
        [
            ft.Text("Create an Account"),
            ft.Container(
                ft.TextField(label="Username", on_change=usernameval),
                alignment=ft.alignment.center,
                padding=50,
            ),
            ft.Container(
                ft.TextField(label="Password", password = True, can_reveal_password=True, on_change=passwordval),
                alignment=ft.alignment.center,
                padding=50,
            ),
            ft.Container(
                ft.FilledButton(text="Create Your Account"),
                alignment=ft.alignment.center,
                padding=50,
                on_click=verifyregister
            ),
        ]
    )