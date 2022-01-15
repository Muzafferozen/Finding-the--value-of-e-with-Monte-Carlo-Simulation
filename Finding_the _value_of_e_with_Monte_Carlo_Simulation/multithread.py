from FindEulerNumber import TicToc, FindEulerNumber

import os

from threading import Thread

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    n = 10000000
    find_numbers_euler = []
    threads = []

    for i in range(os.cpu_count()):
        find_numbers_euler.append(FindEulerNumber())
        threads.append(Thread(target=find_numbers_euler[i].number_more_than_one, args=(n,)))
        print("Started thread number #%d " % i)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    count = 0
    part = 0

    for find_euler in find_numbers_euler:
        count += find_euler.x
        part += find_euler.y

    print("EULER NUMBER = %.8f | COUNT / PART = %d / %d | TIME = %.5f seconds"
          % (count / part, count, part, tt.toc()))

