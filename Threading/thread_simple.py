import threading
import time

def worker():
    """tread worker function"""
    print "%s----", time.ctime()
    return

threads = list()
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()

