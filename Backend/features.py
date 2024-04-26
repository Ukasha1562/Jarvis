from playsound import playsound
import eel
from Backend.speak import talk
import os
import pywhatkit as kit
import re
import webbrowser
import sqlite3
import pvporcupine
import pyaudio
import struct
import time
import pyautogui as autogui
from Backend.helper import extract_from_search
# databse connectivity
con= sqlite3.connect("apps.db")
cur=con.cursor()


# Starting sound
@eel.expose
def start_sound():
  sound="Frontend\\resources\\audio\\start_sound.mp3"
  playsound(sound)

# for opening system apps:
def openCommand(query):
  query=query.replace("open","")
  app_name=query.strip()

  if app_name!="":

    try:
      cur.execute('SELECT path FROM system_apps WHERE name=(?)',(app_name,))
      results=cur.fetchall()

      if len(results)!=0:
        talk("opening "+query)
        os.startfile(results[0][0])

      if len(results)==0:
        cur.execute('SELECT url FROM websites WHERE name=(?)',(app_name,))
        results=cur.fetchall()

        if len(results)!=0:
          talk("opening "+query)
          webbrowser.open(results[0][0])
        else:
          talk("opening "+query)
          try:
            os.system("start "+query)
          except:
            talk("Not found!")
      
    except:
      talk("Something went wrong!")
  else:
    talk("Not found!")



# for opening youtube:
def openyt(query):
  search= extract_from_search(query)
  talk("Playing "+search+" on YouTube")
  kit.playonyt(search)


# for hot word dtection
def hotword():
  porcupine=None
  paud=None
  audio_stream=None

  try:
    porcupine=pvporcupine.create(keywords=["jarvis"])
    paud=pyaudio.PyAudio()
    audio_stream=paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)

    while True:
      keyword=audio_stream.read(porcupine.frame_length)
      keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

      keyword_index=porcupine.process(keyword)

      if keyword_index==0:
        print("hotword dtected!")

        # pressing hotword key virtually to invoke js function for hot word
        autogui.keyDown("win")
        autogui.press('j')
        time.sleep(2)
        autogui.keyUp("win")

  except:
    if porcupine is not None:
      porcupine.delete()
    if audio_stream is not None:
      audio_stream.close()
    if paud is not None:
      paud.terminate()
    