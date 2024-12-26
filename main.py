# import the main function
from modules.ai import AI
# library to detect changes on files
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# others ...
import time
import sys
import os

# cooldown to delay changes detection
cooldown = int(os.environ["COOLDOWN"])

# load the excluded directirues
excluded_dirs = os.environ["EXCLUDED"].split(' ')

# start the AI with the current file
ai = AI()


# listener to changes on files
class ChangeHandler(FileSystemEventHandler):
    # when a file is modified
    def on_modified(self, event):
        if not event.is_directory:
            # check that the file isn't in an excluded dir
            if True not in [d in event.src_path for d in excluded_dirs]:
                # an alert
                print(f"\n>> Detected change on {event.src_path}")
                # and the AI
                ai(event.src_path)

# function to start the listener
def monitor_directory(path):
    # instances
    event_handler = ChangeHandler()
    observer = Observer()
    # also listen on subdirectories
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(cooldown)
    except KeyboardInterrupt:
        observer.stop()
        print("\nWatson AI stopped.")
    observer.join()


# start the listener
monitor_directory(sys.argv[1])