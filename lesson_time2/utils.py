import time
from random import shuffle

def create_random_list(n):
    rlist = list(range(n))
    shuffle(rlist)
    return rlist


def test_time(function, repeat=1):
    times = {}
    for length in range(1000, 10000, 1000):
        t = 0
        for _ in range(repeat):
            my_list = create_random_list(length)
            start = time.time()
            result = function(my_list)
            end = time.time()
            t += end-start 
        print(f"Time for length {length} is {t:.6f} seconds")
        times[length] = t
    print()
    return times
