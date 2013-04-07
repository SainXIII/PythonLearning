import threading
import time
import logging

logging.basicConfig(
        level=logging.DEBUG,
        format="(%(threadName)-10s) %(message)s",
        )

def daemon():
    logging.debug("Starting")
    time.sleep(2)
    logging.debug("Exiting")

def non_daemon():
    logging.debug("Starting")
    logging.debug("Exiting")

d = threading.Thread(name="daemon", target=daemon)
d.setDaemon(True)

t = threading.Thread(name="non-daemon", target=non_daemon)

t.start()
d.start()

t.join()
d.join(1)
