from playsound import playsound
import eel
from Backend.speak import talk
import os
import pywhatkit as kit
import re
import webbrowser
import sqlite3

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

def extract_from_search(ytprompt):
  pattern= r'play\s+(.*?)\s+on\s+youtube'
  match= re.search(pattern, ytprompt, re.IGNORECASE)
  return match.group(1) if match else None