from watchdog.observers import Observer 
import time
from watchdog.events import FileSystemEventHandler
import os
import json


class MyHandler(FileSystemEventHandler):
    i=1
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            src=folder_to_track + "/" + filename
            new_destination=folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = '/Users/rsgado/Documentos/Python/OpenCV exercises'
folder_destination = '/Users/rsgad/OneDrive/Mestrado/Mestrado 1º ano/1º Semestre/SI/OpenCv exercises'
event_handler=MyHandler()
observer=Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

