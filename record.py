import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
import json
import os
import constants


def create_folder():
    if not os.path.isdir(constants.FOLDER_NAME):
        os.mkdir(constants.FOLDER_NAME)


class Record:
    def __init__(self):
        create_folder()
        self.count = 0
        self.coordinates = []


    def print(self):
        x, y = pg.position()
        photo = pg.screenshot(region=(x-3, y-3, 6, 6))
        path = f"{constants.FOLDER_NAME}/flag_{self.count}.png"
        photo.save(path)
        self.count +=1
        infos = {
            "path" : path,
            "down_hole" : 0,
            "up_hole" : 0,
            "up_hole_path": "",
            "wait" : 10,
            "plusx": 0,
            "plusy": 0
        }
        self.coordinates.append(infos)

    def update_coordinates(self, info, value = 1):
        last_coordinate = self.coordinates[-1]
        last_coordinate[info] = value
    
    def key_code(self, key):
        if key == keyboard.Key.esc:
            with open(f"{constants.FOLDER_NAME}/infos.json", "w") as file:
                file.write(json.dumps(self.coordinates))
            return False
        elif key == keyboard.Key.insert:
            self.print()
        elif key == keyboard.Key.page_down:
            self.update_coordinates("down_hole")
        elif key == keyboard.Key.page_up:
            self.update_coordinates("up_hole")
        
    def start(self):
        with Listener(on_press = self.key_code) as listener:
            listener.join()


rec = Record()
rec.start()