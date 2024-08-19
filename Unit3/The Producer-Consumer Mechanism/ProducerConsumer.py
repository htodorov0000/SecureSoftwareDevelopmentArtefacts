import threading
from queue import Queue

lock = threading.Lock()
q = Queue()
final_results = []
 
def producer():
    for i in range(100):
        q.put(i)
        
 
def consumer():
    while True:
        lock.acquire(blocking = False) #use lock to prevent race condition
        number = q.get()
        lock.release() #release lock allowing queue access to other threads
        result = (number, number**2)
        final_results.append(result)
        q.task_done()
   
   
for i in range(5):
    t = threading.Thread(target=consumer)
    t.daemon = True
    t.start()
    
producer()

q.join()

print (final_results)
