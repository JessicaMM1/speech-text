# Example 

import threading, queue
import time

q = queue.Queue()

def worker():
    print("worker")
    
    while True:
        # print("while")
        item = q.get()
        # print("after get")
        print(f'{threading.current_thread().name} working on {item}')
        print(f'Finished {item}')

        q.task_done()   


def worker2():
    print("worker2")
    
    # time.sleep(0.5)

    while True:
        print("while2")
        item = q.get(block=True)
        print(f'{threading.current_thread().name} working on {item}')
        print(f'2Finished {item}')

        q.task_done()   

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()
threading.Thread(target=worker2, daemon=True).start()
# threading.Thread(target=worker2, daemon=True).start()
# print("here")
# Send thirty task requests to the worker.
for item in range(15):
    q.put(item)
# print("after for")
# Block until all tasks are done.
q.join()
print('All work completed')
