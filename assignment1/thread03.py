# extending the Thread class
from time import sleep, ctime
from threading import Thread

# a custom fuction that blocks for a moment
class CustomThread(Thread):
    # override the fun function
    def run(self):
        # block for a moment
        sleep(1)

        # display a message
        print(f"{ctime()} This is coming from another thread")

# create a thread
thread = CustomThread()

# run the thread
thread.start()

# wait for the thread to finish
print(f"{ctime()} Waiting for the thread...")

thread.join()