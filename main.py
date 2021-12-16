import getpass
import os
import sys
import ctypes
import random

class Main:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        for root, directories, files in os.walk(os.path.join(self.path, 'backgrounds')):
            self.backgrounds = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]

        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(self.path, 'backgrounds', random.choice(self.backgrounds)) , 0)

application = Main()