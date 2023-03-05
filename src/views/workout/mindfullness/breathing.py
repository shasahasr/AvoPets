
from time import sleep
import flet as ft


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

    def animate(e):
        if c.content == c1:
            c.content = c2
        else:
            c.content = c1

        c1.border_radius = ft.border_radius.all(400)
        c2.border_radius = ft.border_radius.all(400)
        c.update()
        """
        sleep(5.5)
        c.content = c2
        c2.border_radius = ft.border_radius.all(400)
        c.update()"""

    button = ft.ElevatedButton("Start", on_click=animate)
    c3 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Exhale as it expands, inhale as it shrinks."), c, button]
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
