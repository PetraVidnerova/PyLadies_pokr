import random
import time

from utils import yes_or_no

def gen_exercise():
    a, b = random.randrange(0, 11), random.randrange(0, 11)
    return a, b, a*b


def exercise():
    while True:
        a, b, result = gen_exercise() 
        try:
            s = time.time()
            answer = int(input(f"{a:>2} * {b:>2} = "))
            e = time.time()
            answer_time = e-s
        except ValueError:
            continue
        break
    if answer == result:
        return True, answer_time
    else:
        return False, answer_time

        

    
def game():
    correct, incorrect = 0, 0
    total_time = 0
    while True:
        for _ in range(5):
            correct_answer, answer_time = exercise()
            if correct_answer:
                correct += 1
                total_time += answer_time
                print(" \N{PARTY POPPER} ")
            else:
                incorrect += 1
                print(" \N{SKULL} ")

        if yes_or_no("Chceš končit?"):
            break

    return correct, incorrect, total_time/correct
        

