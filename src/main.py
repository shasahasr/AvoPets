import flet as ft
from views.home import home
from views.login import login
from views.create_account import create_account
from views.train import train
from views.workout.weight.push import push
from views.workout.weight.pull import pull
from views.workout.weight.cardio import cardio
from views.workout.weight.leg import leg
from views.battle import battle
from views.profile import profile


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.client_storage.clear()

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
        if page.route == "/pull":
            page.views.append(pull(page))
        if page.route == "/cardio":
            page.views.append(cardio(page))
        if page.route == "/leg":
            page.views.append(leg(page))
        if page.route == "/breathing":
            page.views.append(leg(page))
        if page.route == "/meditation":
            page.views.append(leg(page))
        if page.route == "/yoga":
            page.views.append(leg(page))
        if page.route == "/sleep":
            page.views.append(leg(page))
        if page.route == "/logout":
            page.client_storage.clear()
            page.go('/')
        if page.route == "/profile":
            page.views.append(profile(page))
        if page.route == "/battle":
            page.views.append(battle(page))

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.WEB_BROWSER)
