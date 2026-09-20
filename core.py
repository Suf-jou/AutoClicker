import pyautogui
import threading
from time import sleep
class autoclicker():
    def __init__(self):
        self.running = False
        self.interval = 0.1

    def click(self):
        pyautogui.click()
        print("Clicked at position:", pyautogui.position())

    def stop(self):
        self.running = False

    def loop(self):
        while self.running:
            self.click()
            sleep(self.interval)

    def set_interval(self, interval):
        self.interval = interval

    def start(self):
        sleep(1)  # Optional: Wait for 1 second before starting
        self.running = True
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()