from random import random
import keyboard

import pyautogui
import threading
from time import sleep
class autoclicker():
    def __init__(self):
        self.running = False
        self.interval = 0.1
        self.randomise = False
        self.on_stop = None

    def click(self):
        pyautogui.click()
        print("Clicked at position:", pyautogui.position())

    def stop(self):
        self.running = False
        if self.on_stop is not None:
            self.on_stop()

    def loop(self):
        while self.running:
            if keyboard.is_pressed("shift"):
                self.stop()
                break
              
            self.click()
            if self.randomise:
                sleep(self.interval + (self.interval * 0.5 * (2 * random.random() - 1)))  # Randomize interval by ±50%
            else:
                sleep(self.interval)

    def set_interval(self, interval):
        self.interval = interval

    def toggle_randomization(self):
        if self.randomise:
            self.randomise = False
        else:
            self.randomise = True

    def start(self):
        sleep(1)  # Optional: Wait for 1 second before starting
        self.running = True
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()