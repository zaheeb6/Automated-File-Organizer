import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileOrganizer(FileSystemEventHandler):
    def __init__(self, folder_to_track):
        self.folder_to_track = folder_to_track
        
    def on_modified(self, event):
        for filename in os.listdir(self.folder_to_track):
            src = os.path.join(self.folder_to_track, filename)
            if os.path.isfile(src):
                file_extension = filename.split('.')[-1].lower()
                dest_folder = os.path.join(self.folder_to_track, file_extension)
                
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                
                shutil.move(src, os.path.join(dest_folder, filename))
                print(f"Moved {filename} to {file_extension} folder")

def main():
    folder_to_track = os.path.expanduser("~/Downloads")  # Change this to your preferred folder
    event_handler = FileOrganizer(folder_to_track)
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()