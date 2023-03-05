from time import sleep
import flet as ft
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current))))
sys.path.append(parent)
from firebase import *

def breathing(page: ft.Page):
    c1 = ft.Container(
        # ft.Text("Inhale", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=400,
        height=400,
        bgcolor=ft.colors.CYAN,
    )

    c2 = ft.Container(
        # ft.Text("Exhale", size=ft.TextThemeStyle.HEADLINE_MEDIUM),
        alignment=ft.alignment.center,
        width=400,
        height=400,
        bgcolor=ft.colors.CYAN,
    )
    c1.border_radius = ft.border_radius.all(400)
    c2.border_radius = ft.border_radius.all(400)

    c = ft.AnimatedSwitcher(
        c2,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=6000,
        reverse_duration=6000,
    )
    c3 = ft.Container(
        content=c,
        alignment=ft.alignment.center
    )

    dlg = ft.AlertDiolog(
        title=ft.Text("Information about breathing: "),
        content=ft.Text(
        """
        When you breathe deeply, the air coming in through your nose fully fills your lungs, and the lower belly rises. Deep abdominal breathing encourages full oxygen exchange — that is, the beneficial trade of incoming oxygen for outgoing carbon dioxide. Not surprisingly, it can slow the heartbeat and lower or stabilize blood pressure.

        Information from: https://www.health.harvard.edu/mind-and-mood/relaxation-techniques-breath-control-helps-quell-errant-stress-response
        """
    ))

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    def animate(e):
        if c.content == c1:
            c.content = c2
        else:
            c.content = c1

        c1.border_radius = ft.border_radius.all(400)
        c2.border_radius = ft.border_radius.all(400)
        c.update()
        add_xp(page.client_storage.get("user_id"), 5)
        add_health(page.client_storage.get("user_id"), 5)

    button = ft.ElevatedButton("Start", on_click=animate)
    dlgbutton = ft.ElevatedButton("Know More About Breathing", on_click=open_dlg)
    c3 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Exhale as it expands, inhale as it shrinks."), c, fr.Row([button, dlgbutton])]
        ),
        alignment=ft.alignment.center
    )
    return ft.View(
        '/breathing',
        [
            ft.AppBar(title=ft.Text('Meditation'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            c3,
        ]
    )
