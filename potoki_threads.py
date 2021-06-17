# import threading
import time
import random
import multiprocessing

# def worker(number):
#     sleep = random.randrange(1, 10)
#     time.sleep(sleep)
#     print("i am worker {}, I slept for {} seconds".format(number, sleep))
#
#
# for i in range(1, 6):
#     t = threading.Thread(target=worker, args=(i, ))
#     t.start()
#
# print("All threads are queued, les's see when they finish!")


##############################################################


def worker(number):
    sleep = random.randrange(1, 10)
    time.sleep(sleep)
    print("i am worker {}, I slept for {} seconds".format(number, sleep))


for i in range(1, 6):
    t = multiprocessing.Process(target=worker, args=(i, ))
    t.start()

print("All threads are queued, les's see when they finish!")