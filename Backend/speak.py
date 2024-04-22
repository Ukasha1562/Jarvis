# Libraries
import pyttsx3
import speech_recognition as sr
import eel

# speaking function
def talk(prompt):
  engine = pyttsx3.init()
  engine.setProperty('rate',174)
  engine.say(prompt)
  engine.runAndWait()


# Speech to text function
@eel.expose
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
    talk(query)
    eel.ShowShape()
  except Exception as e:
    return ""
  return query.lower()


