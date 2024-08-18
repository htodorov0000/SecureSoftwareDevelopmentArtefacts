import threading
from queue import Queue

semaphore = threading.Semaphore()
q = Queue()
final_results = []
 
def producer():
    for i in range(100):
        q.put(i)
        
 
def consumer():
    while True:
        semaphore.acquire() #use semaphore to prevent race condition
        number = q.get()
        semaphore.release() #release semaphore allowing queue qccess to other threads
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
