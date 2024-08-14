import os
import signal
import time
from threading import Thread
from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.keyboard import Key, KeyCode
from PIL import Image
from utils import KEYCODE_W, is_wasd

_ICO = 'foxhole.ico'
_NAME = 'Foxhole Auto'


class Foxhole:
    def __init__(self):
        self.controller = FoxholeController()

    def start(self):
        self.controller.start()

    def stop(self):
        self.controller.stop()

class FoxholeController:
    def __init__(self):
        self.scroop = False
        self.holding_w = False
        self.arty = False
        self.logi_collect = False
        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        self.spam_lmb_thread = None
        self.arty_thread = None
        self.logi_collect_thread = None
        self.mouse_listener = mouse.Listener(
            on_click=self.on_click_handler
        )
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_key_press_handler,
            on_release=self.on_key_release_handler
        )

    def start(self):
        print("Listening for input... Press Ctrl+C to exit.")
        self.mouse_listener.start()
        self.keyboard_listener.start()

    def stop(self):
        self.mouse_listener.stop()
        self.keyboard_listener.stop()

    def on_click_handler(self, x: int, y: int, button: Button, pressed: bool):
        if button == Button.right and pressed and self.arty:
            # Stop Arty
            self.toggle_arty()
        elif button == Button.right and pressed and self.logi_collect:
            # Stop Logistics (Collect Materials)
            self.toggle_logi_collect()

    def on_key_press_handler(self, key: (Key | KeyCode | None)):
        if key == Key.f2:
            # Toggle Scrooping
            self.toggle_scroop()
        elif key == Key.f3:
            # Toggle Logistics (Move Forward)
            self.toggle_move_forward()
        elif key == Key.f4:
            # Toggle Logistics (Collect Materials)
            self.toggle_logi_collect()
        elif key == Key.f5:
            # Toggle Arty
            self.toggle_arty()
        elif is_wasd(key) and self.scroop:
            # Stop Scrooping
            self.toggle_scroop()
        elif is_wasd(key) and self.logi_collect:
            # Stop Logistics (Collect Materials)
            self.toggle_logi_collect()
        elif is_wasd(key) and self.arty:
            # Stop Arty
            self.toggle_arty()

    def on_key_release_handler(self, key: (Key | KeyCode | None)):
        if key == KEYCODE_W and self.holding_w:
            # Stop Logistics (Move Forward)
            self.toggle_move_forward()

    def toggle_scroop(self):
        def start_scroop():
            while self.scroop:
                self.mouse.click(mouse.Button.left)
                time.sleep(0.4)

        self.scroop = not self.scroop
        if self.scroop:
            print("Start Scrooping")
            self.spam_lmb_thread = Thread(target=start_scroop)
            self.spam_lmb_thread.start()
        else:
            # wait for spam_lmb thread to finish
            if self.spam_lmb_thread is not None:
                print("Stopped Scrooping")
                self.spam_lmb_thread.join()
                self.spam_lmb_thread = None

    def toggle_move_forward(self):
        self.holding_w = not self.holding_w
        if self.holding_w:
            print("Start Moving Forward")
            self.keyboard.press('w')
        else:
            print("Stopped Moving Forward")
            self.keyboard.release('w')

    def toggle_arty(self):
        def start_arty():
            while self.arty:
                self.keyboard.press('r')
                time.sleep(0.1)
                self.keyboard.release('r')
                self.mouse.click(Button.left)
                time.sleep(0.1)
                self.mouse.release(Button.left)
                time.sleep(1)

        self.arty = not self.arty
        if self.arty:
            print("Start Arty")
            self.arty_thread = Thread(target=start_arty)
            self.arty_thread.start()
        else:
            # wait for arty thread to finish
            if self.arty_thread is not None:
                print("Stopped Arty")
                self.arty_thread.join()
                self.arty_thread = None

    def toggle_logi_collect(self):
        def start_logi_collect():
            while self.logi_collect:
                self.keyboard.press(Key.shift)
                time.sleep(0.1)
                self.mouse.click(Button.left)
                time.sleep(0.1)
                self.mouse.release(Button.left)
                self.keyboard.release(Key.shift)
                time.sleep(1)

        self.logi_collect = not self.logi_collect
        if self.logi_collect:
            print("Start Logi Collect")
            self.logi_collect_thread = Thread(target=start_logi_collect)
            self.logi_collect_thread.start()
        else:
            # wait for logi collect thread to finish
            if self.logi_collect_thread is not None:
                self.logi_collect_thread.join()
                self.logi_collect_thread = None
                print("Stop Logi Collect")


def build() -> Foxhole:
    return Foxhole()
