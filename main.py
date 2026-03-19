import pyautogui as pg
import time
import keyboard

pg.useImageNotFoundException()
REGION_BATTLE = (1193, 413, 172, 55)
REGION_LOOT = (499, 231, 138, 137)

POSITION_MANA = (600, 32)
COLOR_MANA = (0, 63, 140)

POSITION_LIFE = (190, 33)
COLOR_LIFE_SAFE = (109, 157, 4)
# 100 145 4
# COLOR_LIFE_DANGER
#COLOR_LIFE_CRITICAL


# desabilita UI tibia, para fins de claridade visual do bot
# pg.hotkey('ctrl', 'n')

def check_battle():
    return pg.locateOnScreen("imgs/region_battle.PNG", region=REGION_BATTLE)

# time.sleep(2)
# battle = check_battle()
# print(battle)

def kill_monsters():
    while True:
        # wait 0.5s
        get_loot()
        print("ta no whi le de kirk monsters")
        keyboard.wait("h")
        try:
            battle = check_battle()
            print(battle)
        except pg.ImageNotFoundException:
            pg.press("space")
            while True:
                try:
                    pg.locateOnScreen("imgs/red_target.PNG", confidence=0.95, region=REGION_BATTLE)
                    print("esperando o monstro morrer")
                except pg.ImageNotFoundException:
                    print("paro de ataca zé")
                    break


def get_loot_old():
    loot = pg.locateAllOnScreen("imgs/dead_monster.PNG", confidence=0.9, region=REGION_LOOT)
    for box in loot:
        x, y = pg.center(box)
        pg.moveTo(x, y)
        pg.click(button="right")

def get_loot():
    pg.hotkey('alt', 'q')


def check_status(delay, mousePosX, mousePosY, colorToMatch, buttonToPress):
    pg.sleep(delay)
    if(pg.pixelMatchesColor(mousePosX, mousePosY, colorToMatch)):
        pg.press(buttonToPress)
        print("match")
    else:
        print("no match")

def eat_food():
    pg.press("F6")
    print("comendo food...")



# pg.displayMousePosition()
# check_status(5, *POSITION_MANA, COLOR_MANA , 'F3')
# check_status(1, *POSITION_LIFE, COLOR_LIFE_SAFE, 'F3')
