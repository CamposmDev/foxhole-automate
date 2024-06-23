from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageTk
import os
import threading
from signal import SIGINT
import tkinter

_ICO = 'assets/foxhole.ico'
_NAME = 'Foxhole Auto'

class SysTray:
    def __init__(self):
        self.settings_win = None
        self._settings_thread = None
        self._icon_thread = None
        self.show_notifications = False
        self.image = Image.open(_ICO)
        # TODO - Implement Settings
        # mi_settings = MenuItem('Settings', self._settings)
        mi_exit = MenuItem('Exit', self._stop)
        self.icon = Icon(_NAME, self.image, 
            menu=Menu(
                # mi_settings, 
                mi_exit
            ), 
            title=_NAME)

    def _settings(self, icon, item):
        if self.settings_win:
            self.settings_win.deiconify()
            self.settings_win.lift()
        else:
            self.settings_win = tkinter.Tk()
            self.settings_win.iconphoto(True, ImageTk.PhotoImage(self.image))
            self.settings_win.title(_NAME)
            self.settings_win.resizable(False, False)
            self.settings_win.geometry("500x300")

            label = tkinter.Label(self.settings_win, text='Settings')
            label.pack(pady=8)
            self.settings_win.mainloop()

    def _stop(self, icon, item):
        '''
        Sends SIGINT to itself to terminate.
        '''
        os.kill(os.getpid(), SIGINT)

    def show(self):
        self._icon_thread = threading.Thread(target=self.icon.run)
        self._icon_thread.start()

    def stop(self):
        self.icon.stop()