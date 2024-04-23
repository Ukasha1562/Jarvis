from playsound import playsound
import eel
from Backend.speak import talk
import os
import pywhatkit as kit
import re

# Starting sound
@eel.expose
def start_sound():
  sound="Frontend\\resources\\audio\\start_sound.mp3"
  playsound(sound)

# for opening system apps:
def openCommand(query):
  query=query.replace("open","")

  if query!="":
    talk("Opening "+query)
    os.system('start '+query)
  else:
    talk("not found!")

# for opening youtube:
def openyt(query):
  search= extract_from_search(query)
  talk("Playing "+search+" on YouTube")
  kit.playonyt(search)

def extract_from_search(ytprompt):
  pattern= r'play\s+(.*?)\s+on\s+youtube'
  match= re.search(pattern, ytprompt, re.IGNORECASE)
  return match.group(1) if match else None