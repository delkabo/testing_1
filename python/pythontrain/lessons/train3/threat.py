import threading
import time

def sum(a, b):
    print(a + b)
    time.sleep(3)


# print(threading.current_thread())

# print(threading.main_thread())
# threading.main_thread().setName("New Name")
# print(threading.main_thread())

t = threading.Thread(target=sum, args=(3, 5))
t.start()
print("\n")
print(threading.enumerate())
# print(threading.active_count())
t.join