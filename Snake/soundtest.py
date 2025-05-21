import winsound
import time


winsound.PlaySound(r"C:\Users\Devon\Documents\GITREPOS\Python\Snake\theafternoon.wav",
                   winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass


