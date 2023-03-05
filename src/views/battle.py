import flet as ft 
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from firebase import *
from random import randint

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

    global p_health
    global p_endurance
    global b_health
    
    user = get_user_by_id(page.client_storage.get("user_id"))
    boss_health = user.get("pet")["currentlevel"] * 150
    boss_strength = user.get("pet")["currentlevel"] * 125
    user_health = user.get("pet")["health"]
    user_endurance = user.get("pet")["endurance"]
    user_strength = user.get("pet")["strength"]
    user_block = False
    boss_block = False

    p_health = ft.Text("Health: " + str(user_health) + "/" + str(user.get("pet")["health"]))
    p_endurance = ft.Text("Endurance: " + str(user_endurance))
    b_health = ft.Text("Health: " + str(boss_health))

    def boss_moves():
        global user_health
        global p_health
        global boss_block
        global user_block
        global boss_strength
        global boss_health

        move = randint(1, 5)
        if move < 5 and not user_block:
            user_health -= (boss_strength / 10 % boss_health) + randint(0, 15)
            p_health.value = "Health: " + str(user_health) + "/" + str(user.get("pet")["health"])
            page.update()
            print("attacked")
        elif move == 5:
            boss_block = True
            print("block")
        else:
            user_block = False

    def punch(e):
        global boss_block
        global user_endurance
        global boss_health
        global user_strength
        global b_health

        if not boss_block:
            boss_health -= user_strength / 10 + randint(1, 10)
            user_endurance -= 10
            b_health.value = "Health: " + str(boss_health)
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

        if not boss_block:
            boss_health -= user_strength / 7.5 + randint(1, 10)
            user_endurance -= 20
            b_health.value = "Health: " + str(boss_health)
            page.refresh()
        boss_moves()

    return ft.View(
        "/battle",
        [
            ft.AppBar(title=ft.Text('Battle'), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        ft.Text("PLAYER AVOCADO", size = 50),
                        p_health,
                        p_endurance,
                    ]),
                    alignment=ft.alignment.top_left
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("BOSS AVOCADO", size = 50),
                        b_health
                    ]),
                    alignment=ft.alignment.top_left
                )
            ]),
            ft.Divider(),
            ft.Row([
                ft.ElevatedButton("Punch", width=page.width/2, height=100, on_click=punch),
                ft.ElevatedButton("Fork", width=page.width/2, height=100, on_click=fork),
            ]),
            ft.Row([
                ft.ElevatedButton("Block", width=page.width/2, height=100),
                ft.ElevatedButton("Run", width=page.width/2, height=100),
            ]),
        ]
    )