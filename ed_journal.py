import glob
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class JournalWatcher:

    def __init__(self, path, latest):
        self.path = path
        self.latest = latest
        self.observer = Observer()

    def run(self):
        filename = None
        event_handler = EventHandler(filename)
        self.observer.schedule(event_handler, self.path, recursive=False)
        self.observer.start()
        if filename:
            print("Current file: " + filename)
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Watch stopped")

        self.observer.join()

class EventHandler(FileSystemEventHandler):

    def __init__(self, filename):
        self.filename = filename

    def on_any_event(self, event):
        if event.is_directory:
            return None

        elif event.event_type == "created":
            print("Journal %s created" % event.src_path)
            self.filename = event.src_path

        elif event.event_type == "modified":
            print("Journal %s modified" % event.src_path)

# class JournalWatcher

def journal_last_updated(path):
    ls_pattern = path + "/Journal.*.log"
    ls = glob.glob(ls_pattern)
    if ls:
       latest_file = max(ls, key=os.path.getmtime)
       return latest_file

def journal_show_events(path, events):
    jfn = journal_last_updated(path)
    if not jfn:
        return

    jw = JournalWatcher(path, jfn)
    jw.run()
