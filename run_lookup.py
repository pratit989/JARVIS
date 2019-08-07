import threading

import search_file_system


class RunLookup(object):
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        # thread.daemon = True                             # Daemonize thread
        thread.start()

    def run(self):
        """Method that runs forever"""
        search_file_system.read_dir()

        # time.sleep(self.interval)
