import pyautogui
from time import sleep
class autoclicker():
    def __init__(self):
        self.running = False
        self.interval = 0.1

    def click(self):
        pyautogui.click()

    def stop(self):
        self.running = False

    def loop(self):
        while self.running:
            self.click()
            sleep(self.interval)

    def set_interval(self, interval):
        self.interval = interval

    def start(self):
        self.running = True
        self.loop()