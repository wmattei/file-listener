import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


# ! Change this properties
DIRECTORY_TO_WATCH = "/home/wagner/Documents/projects/westpoint/collums/collums-fe/public/assets/icons"
DIRECTORY_TO_ICON_FILE = "/home/wagner/Documents/projects/westpoint/collums/collums-fe/src/assets/icons.js"


def get_template(filename, pascal_name):
    return """
/*eslint-disable */
export const <pascal_name> = ({ classes, variant, opacity }) => (
    <IconBuilder path="<file_name>" classes={classes} variant={variant} opacity={opacity} />
);
/*eslint-enable */
""".replace("<pascal_name>", pascal_name).replace("<file_name>", filename)

class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):

        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # file_name = os.path.splitext(os.path.basename(event.src_path))[0]
            file_name = os.path.basename(event.src_path)
            pascal_case = ''.join(x for x in os.path.splitext(file_name)[
                                  0].title().replace('-', '').replace('_', '') if not x.isspace())
            icon = get_template(file_name, pascal_case)

            with open(DIRECTORY_TO_ICON_FILE, "a") as myfile:
                myfile.write(icon)
            print("Received created event - %s." % event.src_path)

        # TODO when deleting find the string and remove from file
        # elif event.event_type == 'deleted':


if __name__ == '__main__':
    w = Watcher()
    w.run()
