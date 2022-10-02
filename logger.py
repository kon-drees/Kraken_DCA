import os
from datetime import datetime


class Logger:
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.isfile(file_path):
            with open(file_path, 'w') as fp:
                fp.writelines('\n' + datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + ':      log file created')

    def log(self, text: str):
        with open(self.file_path, 'a') as fp:
            fp.writelines('\n' + datetime.now().strftime('%d-%m-%Y-%H-%M-%S') + f':      {text}')