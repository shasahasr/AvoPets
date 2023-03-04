import flet as ft
from views.home import home
from views.login import login
from views.create_account import create_account
from views.train import train
from views.workout.weight.push import push


def main(page: ft.Page):
    page.title = "Flet counter example"

    def route_change(route):
        page.views.clear()
        page.views.append(home(page))
        if page.route == "/login":
            page.views.append(login(page))
        if page.route == "/create_account":
            page.views.append(create_account(page))
        if page.route == "/train":
            page.views.append(train(page))
        if page.route == "/push":
            page.views.append(push(page))

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)
