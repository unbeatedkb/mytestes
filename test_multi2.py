from multiprocessing import Pool, Manager
import time


def consume(q):
    while True:
        if not q.empty():
            q.get()
            time.sleep(12)


if __name__ == "__main__":

    m = Manager()
    queue = m.Queue(4)
    pool = Pool(4)

    for i in range(4):
        pool.apply_async(consume, (queue,))

    while True:
        print(1)
        queue.put(1)
        print("done")
