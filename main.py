import os

import eel

from Backend.features import start_sound
# from Backend.speak import *


def start():
  eel.init("Frontend")
  start_sound()

  os.system('start msedge.exe --app="http://localhost:8000/index.html"')
  eel.start('index.html',mode=None,host='localhost',block=True)


