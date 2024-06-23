from pystray import Icon, MenuItem, Menu
from PIL import Image
import os
import threading
from signal import SIGINT

_ICO = 'assets/foxhole.ico'
_NAME = 'Foxhole Auto'

class SysTray:
    def __init__(self):
        self.settings_win = None
        self._settings_thread = None
        self._icon_thread = None
        self.show_notifications = False
        self.image = Image.open(_ICO)
        mi_exit = MenuItem('Exit', self._stop)
        self.icon = Icon(_NAME, self.image, 
            menu=Menu(
                # mi_settings, 
                mi_exit
            ), 
            title=_NAME)

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