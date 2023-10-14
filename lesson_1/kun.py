from utils import yes_or_no


class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, b):
        if type(b) == tuple:
            return self.x == b[0] and self.y == b[1]
        else:
            return self.x == b.x and self.y == b.y
        
    def copy(self):
        return Coordinate(self.x, self.y)

class HorsePath():

    horse_moves = [
        Coordinate(2, 1),
        Coordinate(2, -1),
        Coordinate(-2, 1),
        Coordinate(-2, -1),
        Coordinate(1, 2),
        Coordinate(-1, 2),
        Coordinate(1, -2),
        Coordinate(-1, -2)
    ]

    def __init__(self):
        self.path = []

    def copy(self):
        new_path = HorsePath()
        new_path.path = self.path.copy()
        return new_path

    def len(self):
        return len(self.path)
        
    def append(self, pos):
        if pos in self.path:
            return False
        self.path.append(pos.copy())
        return True
    
    def get_pos(self):
        return self.path[-1]

    def leads_to_goal(self, goal):
        return self.path[-1] == goal

    def jump(self):
        new_horse = Coordinate(0, 0)
        
        for move in self.horse_moves:
            new_horse.x = self.get_pos().x + move.x
            new_horse.y = self.get_pos().y + move.y
            yield new_horse

        
class Board():

    def __init__(self, horse, goal, size=8):
        if not (0 <= horse.x < size  and 0 <= horse.y < size):
            raise ValueError("Horse out of board.")
        if not (0 <= goal.x < size and 0 <= goal.y < size):
            raise ValueError("Goal out of board.")

        self.horse = horse
        self.goal = goal
        self.size = size

    def validate_horse(self, horse):
        return 0 <= horse.x < self.size and 0 <= horse.y < self.size
        
    def print_me(self):
        for x in range(self.size):
            for y in range(self.size):
                if (x, y) == self.horse:
                    print("\N{Horse}", end="")
                elif (x, y) == self.goal:
                    print("\N{Crown}", end="")
                else:
                    remainder = 1 if y % 2 == 0 else 0
                    if x % 2 == remainder:
                        print("\N{Black Large Square}", end="")
                    else:
                        print("\N{White Large Square}", end="")
            print()

    def animate_path(self, path):
        for horse in path.path:
            self.horse = horse
            self.print_me()
            if horse != self.goal:
                input(" Press Enter ...")

def main():
    horse = Coordinate(3, 2)
    goal = Coordinate(7,6)
    board = Board(horse, goal)

    path_repo = []

    # path of length 0
    path = HorsePath()
    path.append(horse)
    path_repo.append(path)


    while path_repo:
        path = path_repo.pop(0)

        print(f"Cesta délky {path.len()}. Zkusíme skočit dál.") 
        
        for new_horse in path.jump():
            if not board.validate_horse(new_horse):
                # cesta by vedla mimo hraci pole
                continue
            new_path = path.copy()
            if not new_path.append(new_horse):
                # cesta by se zacyklila
                continue
            if new_path.leads_to_goal(goal):
                print("HURA HURA")
                board.animate_path(new_path)
                if not yes_or_no("Chceš hledat jinou cestu? "):
                    return
            else:
                path_repo.append(new_path)

    print("Žádné další cesty.")
    
if __name__ == "__main__":
    main()
