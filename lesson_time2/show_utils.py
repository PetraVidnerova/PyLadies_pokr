import matplotlib.pyplot as plt 


def plot(list_of_time_results, list_of_labels):
    for result, label in zip(list_of_time_results, list_of_labels):
        plt.plot(result.keys(), result.values(), "o-", label=label)
        plt.legend()
    plt.show()
    
        

