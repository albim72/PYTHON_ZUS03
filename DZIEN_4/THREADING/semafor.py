import threading
import time

semafor = threading.Semaphore(3)

def function_thread(thread_nb):
    print(f'Wątek {thread_nb} próbuje uzyskac dostęp... ')
    semafor.acquire()
    print(f'Wątek {thread_nb} uzyskał dostęp... ')
    time.sleep(3)
    semafor.release()
    print(f'Wątek {thread_nb} zwolnił zasób... ')

for i in range(5):
    threading.Thread(target=function_thread,args=(i,)).start()
  
