from multiprocessing import Pool, Queue
import multiprocessing
import time

def do(q):
    while True:
        if q.empty():
            print("empty")
            time.sleep(0.1)
            continue
        m = q.get()
        print("get:", m)

if __name__ == "__main__":

    p = Pool(3)
    m = multiprocessing.Manager()
    q = m.Queue()
    for i in range(4):
        p.apply_async(do, args=(q,))
        
    while True:
        m = time.time()
        print("put", m)
        q.put(m)

