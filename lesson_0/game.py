from plutimication import game
from utils import menu, login

#import matplotlib.pyplot as plt

def play(name):
    correct, incorrect, time_for_correct = game()
    
    print("Správně: ", "\N{MEDIUM SHADE}"*correct, "\N{HEAVY BLACK HEART}") 
    print("Špatně:  ", "\N{MEDIUM SHADE}"*incorrect, "\N{SKULL}")
    print(f"Průměrný čas: {time_for_correct:.3f} sekund.")
    
    with open(name+".txt", "a", encoding="utf-8") as f:
        print(correct, incorrect, time_for_correct, sep=",", file=f)

def statistics(name):
    correct_percentage = []
    times = [] 

    try:
        with open(name+".txt", "r", encoding="utf-8") as f:
            for line in f:
                correct, incorrect, time_for_correct = map(float, line.split(","))
                correct_percentage.append(100*correct/(correct+incorrect))
                times.append(time_for_correct)
    except FileNotFoundError:
        print("Statistika nenalezana. Asi jsi nový hráč.")
        return
    
    print("Procento správných odpovědí:")
    for i, perc in enumerate(correct_percentage):
        print(f"{i:>3}: ", "\N{MEDIUM SHADE}"*int(perc))

    print("Čas:")
    for i, t in enumerate(times):
        print(f"{i:>3}: ", "\N{Lower one eighth block}"*int(t*10))
    
            
    # option = menu(["Procento správných odpovědí.", "Čas."])
    # if option == 0:
    #     plt.bar(range(len(correct_percentage)), correct_percentage)
    #     plt.show()
    # elif option == 1:
    #     plt.plot(range(len(correct_percentage)), times)
    #     plt.show()
        


            
def main():

    print(" **** Vítej ve hře Nábosilka! **** ")

    name = login()
    
    option = menu(["Hra", "Statistika"])

    if option == 0:
        play(name)
    elif option == 1:
        statistics(name)

    print(" ***** Nashledanou. ***** ")

if __name__ == "__main__":
    main()
