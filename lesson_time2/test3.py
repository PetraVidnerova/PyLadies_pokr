import gzip 
import time 
import random 

from utils import create_random_list

list_of_titles = []
with gzip.open("enwiki-latest-all-titles-in-ns0.gz", "rt", encoding="utf-8") as f:
    for i, line in enumerate(f):
        list_of_titles.append(line.strip())
        
print(len(list_of_titles))

my_title = "PyLadies"

s = time.time()
if my_title in list_of_titles:
    print("Ano, je tam.")
else:
    print("Ne, neni tam.")
e = time.time()
print(f"Trvalo to {e-s:.5f} sekund.")


def find_by_bisect(sorted_list, key):
    s = 0
    e = len(sorted_list)
    length = e
    while length > 0:
        center = s+length//2
        if sorted_list[center] == key:
            return True
        elif sorted_list[center] < key:
            s = center+1
        else: 
            e = center 
        length = e-s
    return False


s = time.time()
if find_by_bisect(list_of_titles, my_title):
    print("Ano, je tam.")
else:
    print("Ne, neni tam.")
e = time.time()
print(f"Trvalo to {e-s:.5f} sekund.")
