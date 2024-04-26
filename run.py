from main import start
from Backend.features import hotword
import multiprocessing

# to run Jarvis
def StartJarvis():
  print("Process 1 is running...")
  start()

# to detect hotword
def listen_hot_word():
  print("\nProcess 2 is running...")
  hotword()


# to run both processes side by side means together
if __name__=='__main__':
  p1=multiprocessing.Process(target=StartJarvis)
  p2=multiprocessing.Process(target=listen_hot_word)
  p1.start()
  p2.start()
  p1.join()

  if p2.is_alive():
    p2.terminate()
    p2.join()

  print("system stop!")

