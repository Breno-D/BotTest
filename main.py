import pyautogui as pg
import json
from pynput.keyboard import Listener
from pynput import keyboard
import threading

import constants
import actions
import my_thread

pg.useImageNotFoundException()



# desabilita UI tibia, para fins de claridade visual do bot
# pg.hotkey('ctrl', 'n')

def kill_monsters():
    get_loot()
    try:
        battle = actions.check_battle()
        return
    except pg.ImageNotFoundException:
        pg.press("space")
        if event_th.is_set():
            return
        while True:
            try:
                pg.locateOnScreen("imgs/red_target.PNG", confidence=0.95, region=constants.REGION_BATTLE)
                if event_th.is_set():
                    return
                print("waiting for monster to die")
            except pg.ImageNotFoundException:
                print("monster dead")
                return kill_monsters()


def get_loot_old():
    loot = pg.locateAllOnScreen("imgs/dead_monster.PNG", confidence=0.9, region=constants.REGION_LOOT)
    for box in loot:
        x, y = pg.center(box)
        pg.moveTo(x, y)
        pg.click(button="right")

def get_loot():
    pg.hotkey('alt', 'q')

def go_to_flag(path, wait):
    flag = pg.locateOnScreen(path, confidence=0.8, region=constants.REGION_MAP)
    x,y = pg.center(flag)
    pg.moveTo(x,y)
    pg.click()
    pg.sleep(wait)

def check_player_position():
    try:
        box = pg.locateOnScreen("imgs/playerinmap.png", confidence=0.8, region=constants.REGION_MAP)
        return True
    except pg.ImageNotFoundException:
        return False


def run():  
    with open(f"{constants.FOLDER_NAME}/infos.json", "r") as file:
        data = json.loads(file.read())
    while not event_th.is_set():
        for item in data:
            if event_th.is_set():
                return
            kill_monsters()
            if event_th.is_set():
                return
            go_to_flag(item['path'], item['wait'])
            if check_player_position():
                kill_monsters()
                if event_th.is_set():
                    return
                go_to_flag(item['path'], item['wait'])
            actions.eat_food()
            kill_monsters()
            actions.hole_down(item['down_hole'], item['up_hole_path'])
            actions.hole_up(item['up_hole'], item['up_hole_path'], item['plusx'], item['plusy'])

def key_code(key, th_group):
    if key == keyboard.Key.esc:
        event_th.set()
        th_group.stop()
        return False
    if key == keyboard.Key.delete:
        th_group.start()
        th_run.start()
    if key == keyboard.Key.home:
        actions.hole_up(1,"SWAMP_VENORE/up_anchor.png", 130, 130)

global event_th
event_th = threading.Event()
th_run = threading.Thread(target=run)

th_full_mana = my_thread.MyThread(lambda: actions.check_status(5, *constants.POSITION_MANA, constants.COLOR_MANA, "F4"))
th_life_down = my_thread.MyThread(lambda: actions.check_status(2, *constants.POSITION_LIFE, constants.COLOR_LIFE_SAFE, "F3"))

group_thread = my_thread.ThreadGroup([th_full_mana, th_life_down])


with Listener(on_press = lambda key: key_code(key, group_thread)) as listener:
    listener.join()




# check_status(5, *POSITION_MANA, COLOR_MANA , 'F3')
# check_status(1, *POSITION_LIFE, COLOR_LIFE_SAFE, 'F3')

#testes : pg.displayMousePosition()