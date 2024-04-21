from playsound import playsound
import eel

# Starting sound
@eel.expose
def start_sound():
  sound="Frontend\\resources\\audio\\start_sound.mp3"
  playsound(sound)