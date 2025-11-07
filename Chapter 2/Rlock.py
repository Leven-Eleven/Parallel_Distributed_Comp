from do_something import do_something
import time
import threading


if __name__ == "__main__":
    size = 10000000
    counts = [5, 10, 15]

    print("\n--------------------Multi-Threading with R-locks--------------------")

    for threads in counts:
        r_lock = threading.RLock()
        jobs = []
        start_time = time.time()

        def execute_task(size, out_list):
            with r_lock:
                do_something(size, out_list)

        for i in range(threads):
            out_list = []
            thread = threading.Thread(target=execute_task, args=(size, out_list))
            jobs.append(thread)

        for t in jobs:
            t.start()
        for t in jobs:
            t.join()

        end_time = time.time()
        print(f"Threads: {threads}, Duration = {end_time - start_time:.2f} s")

    print("\n--------------------All threads completed--------------------")