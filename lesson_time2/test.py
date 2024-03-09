from utils import create_random_list, test_time
from show_utils import plot 


def select_sort(input_list):
    sorted_list = input_list.copy()
    n = len(sorted_list)
    for i in range(n-1): 
        min_index = i    # index of minimum 
        for j in range(i, n):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
    return sorted_list


my_list = create_random_list(100)
print(my_list)

my_list = select_sort(my_list)

print(my_list)



time_result = test_time(select_sort)
time_result2 = test_time(sorted)

plot([time_result, time_result2], ["select_sort", "sorted"])
