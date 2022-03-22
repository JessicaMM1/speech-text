# from multiprocessing import Process

# def hello():
#     print("hello")

# def bye():
#     print("bye")

# print("parent")
# if __name__ == '__main__':

   
#     p = Process(target=hello)
#     print("create process ", p.name)
#     p.start()
#     print("after start")
#     p.join()

# p2 = Process(target=bye)
# print(p2.name)
# # p2.start()
# print("completed")

from multiprocessing import Process
import queue
import os
import time


q = queue.Queue()

# def worker():
#     while True:
#         item = q.get()
#         print(f'Working on {item}')
#         print(f'Finished {item}')
#         q.task_done()

def hello(num):
    print("hello ", num+1)
    time.sleep(0.1)

if __name__ == '__main__':
    print(os.cpu_count())

    for i in range(5):
# Turn-on the worker thread.
        #p = Process(target=worker)
        p = Process(target=hello, args=(i,))
        print(p.name)
        p.start()
        # print("join ", i+1)
        # p.join()


# # Send thirty task requests to the worker.
#     for item in range(30):
#         q.put(item)
#     print("after put")
    
#     p.start()

# # Block until all tasks are done.
    # q.join()
    p.join()
print('All work completed')