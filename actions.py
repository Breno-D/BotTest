import pyautogui as pg
import constants

def eat_food():
    pg.press("F6")
    print("comendo food...")

def hole_down(should_down):
    if(should_down):
        try:
            hole = pg.locateOnScreen("imgs/holeImg.PNG", confidence=0.8) # trocar imagem de buraco depois
            x, y = pg.center(hole)
            pg.moveTo(x, y)
            pg.click()
            pg.sleep(5)
        except pg.ImageNotFoundException:
            print("buraco não encontrado")

def hole_up(should_up, img_anchor, plusx, plusy):
    if(should_up):
        try:
            anchorToUp = pg.locateOnScreen(img_anchor, confidence=0.8)
            x,y = pg.center(anchorToUp)
            pg.moveTo(x + plusx, y + plusy)
            pg.press("F11")
            pg.click()
            pg.sleep(5)
        except pg.ImageNotFoundException:
            print("ancora não encontrada")

def check_status(delay, mousePosX, mousePosY, colorToMatch, buttonToPress):
    pg.sleep(delay)
    if(pg.pixelMatchesColor(mousePosX, mousePosY, colorToMatch)):
        pg.press(buttonToPress)
        print("match")
    else:
        print("no match")


def check_battle():
    return pg.locateOnScreen("imgs/region_battle.PNG", region=constants.REGION_BATTLE)
