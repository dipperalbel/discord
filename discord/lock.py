import threading

class GlobalLocks(object):
    _instance = None
    global_lock=threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalLocks, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance
    #def __init__(self):
    #    self.global_lock=threading.Lock()