import flet as ft

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from firebase import *

usr = ""
password = ""

def login(page: ft.Page):
    if page.client_storage.contains_key("user_id"):
        page.go("/")

    def verifylogin(e):
        global usr
        global password
        user = check_login(usr, password)
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
        '/login',
        [
            ft.AppBar(title=ft.Text("Login")),
            ft.Container(
                ft.TextField(
                    label="Username",
                    on_change= usernameval
                ),
                alignment=ft.alignment.center,
                padding=50,
            ),
            ft.Container(
                ft.TextField(
                    label="Password", password = True, can_reveal_password=True,
                    on_change= passwordval
                ),
                alignment=ft.alignment.center,
                padding=50,
            ),
            ft.Container(
                ft.FilledButton(text="Login"),
                alignment=ft.alignment.center,
                padding=50,
                on_click= verifylogin
            ),
        ]
    )