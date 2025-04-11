import threading
import time

event = threading.Event()

def worker():
    print("Worker: Waiting for event to be set.")
    event.wait()  # 阻塞，直到事件被设置
    print("Worker: Event has been set. Continuing execution.")

def setter():
    time.sleep(2)  # 模拟一些操作
    print("Setter: Setting the event.")
    event.set()  # 设置事件
    time.sleep(2)
    print("Setter: Clearing the event.")
    event.clear()  # 清除事件

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=setter)

t1.start()
t2.start()

t1.join()
t2.join()