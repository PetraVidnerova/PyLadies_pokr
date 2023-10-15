from utils import yes_or_no

SIZE = 8
START = (3, 2)
GOAL = (7, 6)

horse_moves = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2)
]


def horse_jump(horse):
        
    for x, y in horse_moves:
        new_horse = (
            horse[0] + x,
            horse[1] + y
        )
        yield new_horse

def valid_horse(horse):
    return 0 <= horse[0] < SIZE and 0 <= horse[1] < SIZE
        
def print_board(size, horse, goal):
    for x in range(size):
        for y in range(size):
            if (x, y) == horse:
                print("\N{Horse}", end="")
            elif (x, y) == goal:
                print("\N{Crown}", end="")
            else:
                remainder = 1 if y % 2 == 0 else 0
                if x % 2 == remainder:
                    print("\N{Black Large Square}", end="")
                else:
                    print("\N{White Large Square}", end="")
        print()

def animate_path(path):
    for horse in path:
        print_board(SIZE, horse, GOAL)
        if horse != GOAL:
            input(" Stiskni Enter ...")

def main():

    path_repo = []
    path = [START]
    path_repo.append(path)

    while path_repo:
        path = path_repo.pop(0)

        print(f"Cesta délky {len(path)}. Zkusíme skočit dál.") 
        
        for new_horse in horse_jump(path[-1]):
            if not valid_horse(new_horse):
                # cesta by vedla mimo hraci pole
                continue
            new_path = path.copy()
            if new_horse in new_path: 
                # cesta by se zacyklila
                continue
            else:
                new_path.append(new_horse)
            if new_path[-1] == GOAL:
                print("HURA HURA")
                animate_path(new_path)
                if not yes_or_no("Chceš hledat jinou cestu? "):
                    return
            else:
                path_repo.append(new_path)

    print("Žádné další cesty.")
    
if __name__ == "__main__":
    main()
