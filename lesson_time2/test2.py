from utils import create_random_list, test_time
from show_utils import plot

results = []
labels = []

# kolik času stojí zjištění délky seznamu?
res = test_time(lambda x: len(x), repeat=1000)
results.append(res)
labels.append("len")

# kolik času stojí získání i-tého prvku?
res1 = test_time(lambda x: x[60], repeat=1000)
res2 = test_time(lambda x: x[-1], repeat=1000)
results.append(res1)
labels.append("[60]")
results.append(res2)
labels.append("[-1]")

# kolik času stojí přidání prvku na konec seznamu? 
res = test_time(lambda x: x.append("prvek"), repeat=1000)    
results.append(res)
labels.append("append")

# kolik času stojí operace in 
res = result = test_time(lambda x: "prvek" in x, repeat=1000)
results.append(res)
labels.append("in")

#long_list = create_random_list(10_000_000)
# s  = time.time()
# print(5 in long_list)
# e = time.time()
# print(e-s)
# #result[10_000_000] = e-s
#plot([result], ["operace in"])

# kolik času stojí operace index
res = test_time(lambda x: x.index(10), repeat=1000) # prvek ktery tam neni    
results.append(res)
labels.append("index")


# insert 
res = test_time(lambda x: x.insert(10, 10), repeat=1000)
results.append(res)
labels.append("insert")


# del
def smaz(my_list):
    del my_list[0]
res = test_time(smaz, repeat=1000)
results.append(res)
labels.append("del")

plot(results, labels)
