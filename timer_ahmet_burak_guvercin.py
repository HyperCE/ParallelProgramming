import time

class Timer:
    def _init_(self):
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def _enter_(self):
    def __enter__(self):
        self.start_time = time.time()
        return self

    def _exit_(self, exc_type, exc_val, exc_tb):
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
