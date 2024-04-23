# Libraries
import pyttsx3
import speech_recognition as sr
import eel
import time

# speaking function
def talk(prompt):
  engine = pyttsx3.init()
  engine.setProperty('rate',174)
  eel.DisplayMessage(prompt)
  engine.say(prompt)
  engine.runAndWait()


# Speech to text function
def speak_converter():
  recog=sr.Recognizer()

  with sr.Microphone() as source:
    print("Listening...")
    eel.DisplayMessage('Listening...')
    recog.pause_threshold=1
    recog.adjust_for_ambient_noise(source)
    audio=recog.listen(source,10,6)
  
  try:
    print("Recognizing...")
    eel.DisplayMessage('Recognizing...')
    query=recog.recognize_google(audio,language="en-in")
    print(f"user said: {query}")
    eel.DisplayMessage(query) 
    time.sleep(2)
  except Exception as e:
    return ""
  return query.lower()



@eel.expose
# For all prompts:
def AllPrompts():
  query=speak_converter()
  print(query)
  
  if "open" in query:
    from Backend.features import openCommand
    openCommand(query)
  elif "on youtube" in query:
    from Backend.features import openyt
    openyt(query)
  else:
    print("sorry for your request!") 
  
  eel.ShowShape()

