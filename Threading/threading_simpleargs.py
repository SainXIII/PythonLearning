import threading
import time

def worker(num):
    print "Worker: %s", num
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
