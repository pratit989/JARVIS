from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import search_directory
import ast
import os

lookup_dict = search_directory.file_system_dict


class ExampleHandler(PatternMatchingEventHandler):
    @staticmethod
    def get_dup_key(keys):

        count = 0
        for k in keys:
            if k in keys:
                count += 1
        return count

    @staticmethod
    def get_event(event_name, method):

        src = event_name.src_path
        key = src.rsplit('\\')[-1].lower()

        if method == 'on_created':
            lookup_dict.update({key + '_{}'.format(
                ExampleHandler.get_dup_key(lookup_dict.keys())): src})
        elif method == 'on_deleted':
            key_list = lookup_dict.keys()
            try:
                for key in list(key_list):
                    if lookup_dict.get(key) == src:
                        del lookup_dict[key]
            except KeyError:
                pass
        elif method == 'on_moved' or method == 'on_modified':
            key_list = lookup_dict.keys()
            try:
                for key in list(key_list):
                    if lookup_dict.get(key) == src:
                        del lookup_dict[key]
                lookup_dict.update({key + '_{}'.format(
                    ExampleHandler.get_dup_key(lookup_dict.keys())): src})

                dir_txt = {}
                file_name = 'dict.txt'
                if os.path.exists(file_name):
                    with open(file_name, 'r') as f:
                        h = ast.literal_eval(f.read())
                        dir_txt.update(h)
                        f.close()

                    with open(file_name, 'w') as f:
                        dir_txt.update({key + '_{}'.format(
                            ExampleHandler.get_dup_key(lookup_dict.keys())): src})
                        f.write(str(dir_txt))
                        f.close()

            except KeyError:
                pass

    def on_created(self, event):  # when file is created
        ExampleHandler.get_event(event, 'on_created')

    def on_modified(self, event):
        ExampleHandler.get_event(event, 'on_modified')

    def on_deleted(self, event):  # when file is deleted
        ExampleHandler.get_event(event, 'on_deleted')

    def on_moved(self, event):  # when file is moved
        ExampleHandler.get_event(event, 'on_moved')


# search_directory.find()


def lookup():
    observer = Observer()
    event_handler = ExampleHandler(
        ignore_patterns=['*.tmp', '*AppData*', '*Temp*', '*$*', '*ProgramData*', '*__*'])  # create event handler
    # set observer to use created event handler in directory
    observer.schedule(event_handler=event_handler, path='C:\\', recursive=True)
    observer.start()
    observer.join()
