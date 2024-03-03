import time 
import counters
from reader import read_bible_lines

start = time.time()
result1 = counters.count_letters("Hello, PyLadies!")
end = time.time()
print(f"Time for count_letters {end-start:.6f} seconds")

start = time.time()
result2 = counters.count_letters2("Hello, PyLadies!")
end = time.time()
print(f"Time for count_letters2 {end-start:.6f} seconds")

def test_time(function):
    times = {}
    for lines in range(1, 10):
        text = read_bible_lines(lines)
        start = time.time()
        result = function(text)
        end = time.time()
        t = end-start 
        print(f"Time for {lines} lines is {t:.6f} seconds")
        times[lines] = t
    return times

times1 = test_time(counters.count_letters)
times2 = test_time(counters.count_letters2)

import matplotlib.pyplot as plt 

plt.plot(times1.keys(), times1.values(), "o-", label="varianta s count")
plt.plot(times2.keys(), times2.values(), "o-", label="varianta s count")


plt.show()