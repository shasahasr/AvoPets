from random import randint
from time import sleep
from firebase import *
from math import *
import flet as ft
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

boss_health = 0
boss_strength = 0
user_health = 0
user_endurance = 0
user_strength = 0
user_block = 0
boss_block = 0

p_health = None
p_endurance = None
b_health = None


def battle(page: ft.Page):
    global boss_health
    global boss_strength
    global user_health
    global user_endurance
    global user_strength
    global user_block
    global boss_block

    global current_image_container
    global p_health
    global p_endurance
    global b_health
    fork_image = ft.Container(
        content=ft.Image(
            src=f"./assets/fork0.gif",
            width=400,
            height=400,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center
    )
    jab_image = ft.Container(
        content=ft.Image(
            src=f"./assets/right_jab0.gif",
            width=400,
            height=400,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center
    )
    idle_image = ft.Container(
        content=ft.Image(
            src=f"./assets/idle0.gif",
            width=400,
            height=400,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center
    )
    run_image = ft.Container(
        content=ft.Image(
            src=f"./assets/run0.gif",
            width=400,
            height=400,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center
    )
    current_image = idle_image
    current_image_container = [current_image]
    boss_image = ft.Container(
        content=ft.Image(
            src=f"./assets/boss #1.gif",
            width=400,
            height=400,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center
    )

    user = get_user_by_id(page.client_storage.get("user_id"))
    boss_health = 150 + \
        user.get("pet")["currentlevel"] * 50 * (randint(50, 150) / 100)
    boss_strength = user.get("pet")["currentlevel"] * 60 * (randint(50, 150) / 100)
    user_health = user.get("pet")["health"]
    user_endurance = user.get("pet")["endurance"]
    user_strength = user.get("pet")["strength"]
    user_block = False
    boss_block = False

    p_health = ft.Text("Health: " + str(floor(user_health)) +
                       "/" + str(floor(user.get("pet")["health"])))
    p_endurance = ft.Text("Endurance: " + str(floor(user_endurance)))
    b_health = ft.Text("Health: " + str(floor(boss_health)))

    def change_images(string):
        global current_image_container
        print(string)
        if string == "idle":
            current_image_container[0] = idle_image
        else:
            if string == "jab":
                current_image_container[0] = jab_image
                page.update()
                sleep(1)
            elif string == "run":
                current_image_container[0] = run_image
            elif string == "fork":
                current_image_container[0] = fork_image
                page.update()
                sleep(2)
            print(current_image_container[0].content.src)
            page.update()
            sleep(1)
            current_image_container[0] = idle_image
        # page.update()

    def boss_moves():
        global user_health
        global p_health
        global boss_block
        global user_block
        global boss_strength
        global boss_health

        if boss_health < 0:
            add_xp(page.client_storage.get("user_id"),
                   user.get("pet")["currentlevel"] * 30)
            page.go("/")

        move = randint(1, 5)
        if move < 5 and not user_block:
            user_health -= ((boss_strength / 10 % boss_health) +
                            randint(0, 15)) / (user.get("pet")["health"] / 100)
            p_health.value = "Health: " + \
                str(floor(user_health)) + "/" + str(floor(user.get("pet")["health"]))
            if user_health < 0:
                page.go("/")
            page.update()
        elif move == 5:
            boss_block = True
        else:
            user_block = False

    def punch(e):
        global boss_block
        global user_endurance
        global boss_health
        global user_strength
        global b_health
        global p_endurance
        global current_image_container

        change_images("jab")
        
        if user_endurance <= 0:
            page.go("/")

        if not boss_block:
            boss_health -= user_strength / 10 + randint(1, 10)
            user_endurance -= 10
            b_health.value = "Health: " + str(floor(boss_health))
            p_endurance.value = "Endurance: " + str(floor(user_endurance))
            page.update()
        else:
            boss_block = False
        boss_moves()

    def fork(e):
        global boss_block
        global boss_health
        global user_strength
        global user_endurance
        global b_health
        global p_endurance
        global current_image

        if user_endurance <= 0:
            page.go("/")

        change_images("fork")
        if not boss_block:
            boss_health -= user_strength / 5 + randint(1, 10)
            user_endurance -= 15
            b_health.value = "Health: " + str(floor(boss_health))
            p_endurance.value = "Endurance: " + str(floor(user_endurance))
            page.update()
        boss_moves()

    def heal(e):
        global boss_block
        global boss_health
        global user_strength
        global user_health
        global user_endurance
        global b_health
        global p_endurance
        global p_health
        global current_image

        user_health += user.get("pet")["health"] / 10
        user_endurance -= 15
        p_health.value = "Health: " + str(floor(user_health)) + "/" + str(floor(user.get("pet")["health"]))
        p_endurance.value = "Endurance: " + str(floor(user_endurance))
        page.update()
        boss_moves()
        

    def run(e):
        page.go("/")

    return ft.View(
        "/battle",
        [
            ft.AppBar(title=ft.Text('Battle'),
                      bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        ft.Text("PLAYER AVOCADO", size=50),
                        p_health,
                        p_endurance,
                    ], width=page.width/2),
                    alignment=ft.alignment.top_left
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("BOSS AVOCADO", size=50),
                        b_health
                    ], width=page.width/2),
                    alignment=ft.alignment.top_left
                )
            ]),
            ft.Divider(),
            ft.Row([
                ft.ElevatedButton("Punch", width=page.width/2,
                                  height=100, on_click=punch),
                ft.ElevatedButton("Fork", width=page.width/2,
                                  height=100, on_click=fork),
            ]),
            ft.Row([
                ft.ElevatedButton("Heal", width=page.width/2,
                                  height=100, on_click=heal),
                ft.ElevatedButton("Run", width=page.width/2,
                                  height=100, on_click=run),
            ]),
            ft.Row([
                ft.Column(
                    current_image_container,
                    width=page.width/2),
                ft.Column([
                    boss_image
                ], width=page.width/2)
            ]),
        ]
    )
