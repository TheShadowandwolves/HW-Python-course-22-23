import random
import time


#size of the board
WIDTH: int = 10
HEIGHT: int = 10
#battlefield board
HIT_SHIP: str = "|X|"
MISS_SHIP: str = "|O|"
EMPTY_SPACE: str = "|_|"
SUNK_SHIP: str = "|%|"
IS_SHIP: str = "|S|"




class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.image = []
        self.hits = 0
        for i in range(length):
            self.image.append(IS_SHIP)

    def hit(self, position):
        self.hits += 1
        self.image[position] = HIT_SHIP

    def is_sunk(self):
        return self.hits == self.length

class Battlefield:
    def __init__(self, width, height):
        self.width = WIDTH
        self.height = HEIGHT
        self.ships = []
        self.cordinate = [[0 for x in range(WIDTH)] for y in range(HEIGHT)] 
        self.orientation = "horizontal"
        self.hits = 0
        self.misses = 0
        for i in range(self.width):
            for j in range(self.height):
                self.cordinate[i][j] = EMPTY_SPACE

    def check_place(self, ship, a, b, horizontal):
        if horizontal == "vertical":
            if ship.length + b > self.height:
                print("Ship is out of bounds")
                return False
        if horizontal == "horizontal":
            if ship.length + a > self.width:
                print("Ship is out of bounds")
                return False
        if horizontal == "horizontal":
            for i in range(ship.length):
                if self.cordinate[b][a+i] == IS_SHIP:
                    print("Ship is overlapping")
                    return False
        elif horizontal == "vertical":
            for i in range(ship.length):
                if self.cordinate[b+i][a] == IS_SHIP:
                    print("Ship is overlapping")
                    return False
        return True
    def aicheck_place(self, ship, a, b, horizontal):
        if horizontal == "vertical":
            if ship.length + b > self.height:
                return False
        if horizontal == "horizontal":
            if ship.length + a > self.width:
            #print("Ship is out of bounds")
                return False
        if horizontal == "horizontal":
            for i in range(ship.length):
                if self.cordinate[b][a+i] == IS_SHIP:
                    #print("Ship is overlapping")
                    return False
        elif horizontal == "vertical":
            for i in range(ship.length):
                if self.cordinate[b+i][a] == IS_SHIP:
                    #print("Ship is overlapping")
                    return False
        return True

    def if_all_sunk(self):
        for i in self.ships:
            if i.is_sunk() == True:
                return True
        return False

    def add_ship(self, ship, a, b, horizontal):
        if self.check_place(ship, a, b, horizontal) == False:
            return False
        self.ships.append(ship)
        self.orientation = horizontal
        self.draw_ship(a, b, ship)
        
    def draw_ship(self, a, b, ship):
        if self.orientation == "horizontal":
            for i in range(ship.length):
                self.cordinate[b][a+i] = IS_SHIP
        elif self.orientation == "vertical":
            for i in range(ship.length):
                self.cordinate[b+i][a] = IS_SHIP

    def hit_ship(self, x, y):
        if x > self.width or y > self.height:
            return False
        for a in self.cordinate:
            for b in a:
                if self.cordinate[y][x] == IS_SHIP:
                    self.hits += 1
                    self.cordinate[y][x] = HIT_SHIP
                    return True
                else:
                    self.misses += 1
                    self.cordinate[y][x] = MISS_SHIP
                    return False    
            
    def is_hit(self, x, y):
        return self.cordinate[y][x] == HIT_SHIP

    def is_miss(self, x, y):
        return self.cordinate[y][x] == MISS_SHIP
    
    def print_board(self):
        for a in self.cordinate:
            for b in a:
                print(b, end="")
            print()
        return ""
    
    def print_without_ships(self):
        for a in self.cordinate:
            for b in a:
                if b == IS_SHIP:
                    print(EMPTY_SPACE, end="")
                else:
                    print(b, end="")
            print()
        return ""

    def __str__(self):
        for a in self.cordinate:
            for b in a:
                print(b, end="")
            print()
        return ""
#ship types
AIRCRAFT = Ship("Aircraft Carrier", 5)
BATTLESHIP = Ship("Battleship", 4)
SUBMARINE = Ship("Submarine", 3)
CRUISER = Ship("Cruiser", 3)
DESTROYER = Ship("Destroyer", 2)

class Game:
    def __init__(self):
        self.player = Battlefield(WIDTH, HEIGHT)
        self.computer = Battlefield(WIDTH, HEIGHT)
        self.game = True
        self.turn = 1
        self.plklicked = []
        self.aiklicked = []
        self.gotit = []
    
    def intro(self):
        print("Welcome to Battleship!")
        print("You will be playing against the computer.")
        print("You will be given a 10x10 board to place your ships.")
        print("You will be given 5 ships to place on the board.")
        print("The ships are as follows:")
        print("Aircraft Carrier (5 spaces)")
        print("Battleship (4 spaces)")
        print("Submarine (3 spaces)")
        print("Cruiser (3 spaces)")
        print("Destroyer (2 spaces)")
        print("")

    def ai_place(self , ship):
        x = random.randint(0, WIDTH - ship.length)
        y = random.randint(0, HEIGHT- ship.length)
        orientation = random.choice(["horizontal", "vertical"])
        worked = False
        while worked == False:
            if self.computer.aicheck_place(ship, x, y, orientation):
                self.computer.add_ship(ship, x, y, orientation)
                worked = True
                return True
            else:
                x = random.randint(0, WIDTH - ship.length)
                y = random.randint(0, HEIGHT- ship.length)
                orientation = random.choice(["horizontal", "vertical"])
                
            

    def input_ship(self, ship):
        print("Place your", ship.name)
        print("Length:", ship.length)
        self.ai_place(ship)
        print("Horizontal or Vertical?")
        orientation = input()
        if orientation == "horizontal" or orientation == "vertical":
            print("Enter the start x coordinate")
            x = int(input())
            print("Enter the start y coordinate")
            y = int(input())
           
            if self.player.check_place(ship, x, y, orientation):
                self.player.add_ship(ship, x, y, orientation)
                return True
            else:
                return False
            
            
        else:
            print("Invalid input")
            return False

    def insert_all_ship(self):
        while (self.input_ship(AIRCRAFT) == False):
            print("Try again")
        print(self.player.print_board())
        while (self.input_ship(BATTLESHIP) == False):
            print("Try again")
        print(self.player.print_board())
        while (self.input_ship(SUBMARINE) == False):
            print("Try again")
        print(self.player.print_board())
        while (self.input_ship(CRUISER) == False):
            print("Try again")
        print(self.player.print_board())
        while (self.input_ship(DESTROYER) == False):
            print("Try again")
        print("Your board:")
        print(self.player.print_board())
        print(self.computer.print_board())

    def player_turn(self):
        t = 1
        while t == 1:
            print("Enter the x coordinate")
            x = int(input())
            print("Enter the y coordinate")
            y = int(input())
            if x >= 9 or x <= 0 or y >= 9 or y <= 0:
                print("Invalid input")
            
            if self.plklicked == []:
                break

            for i in self.plklicked:
                if i == [x,y]:
                    print("You have already clicked this spot")
                    break
                else:
                    t = 0

        if self.computer.hit_ship(x, y):
            print("Hit!")
            self.plklicked.append([x,y])
            return True
        else:
            print("Miss!")
            self.plklicked.append([x,y])
            return False
        #print(self.player.print_board())
        #print(self.computer.print_without_ships())

    def search_klick(self, num):
        for k in self.aiklicked:
            if num == k:
                return False
        return True

    def ai_search(self):
        if self.aiklicked == []:
            return False

        for i in self.aiklicked:
            if self.player.is_hit(i[0], i[1]):
                self.gotit.append(i)

        for j in self.gotit:
            top = [j[0], j[1] -1]
            bottom = [j[0], j[1] +1]
            left = [j[0]-1, j[1]]
            right = [j[0]+1, j[1]]
            if (self.search_klick(top)):
                return top
            if (self.search_klick(bottom)):
                return bottom
            if (self.search_klick(right)):
                return right
            if (self.search_klick(left)):
                return left
            if not self.search_klick(top) and not self.search_klick(right) and not self.search_klick(bottom) and not self.search_klick(left):
                self.gotit.clear()
            # for k in self.aiklicked:
            #     if j[0] == k[0] and j[1]+1 != k[1]:
            #         return [j[0], j[1] + 1]
            #     elif j[0] == k[0] and j[1]-1 != k[1]:
            #         return [j[0], j[1] - 1]
            #     elif j[1] == k[1] and j[0]+1 != k[0]:
            #         return [j[0] + 1, j[1]]
            #     elif j[1] == k[1] and j[0]-1 != k[0]:
            #         return [j[0] - 1, j[1]]
        return False
                     

    def computer_turn(self):
        t = 1
        while t == 1:
            found = self.ai_search()
            if found != False:
                x = found[0]
                y = found[1]
            else:
                x = random.randint(0, WIDTH - 1)
                y = random.randint(0, HEIGHT - 1)
            if self.aiklicked == []:
                break
            for i in self.aiklicked:
                if i == [x,y]:
                    t = 1
                    break
                else:
                    t = 0
        self.aiklicked.append([x,y])
        if self.player.hit_ship(x, y):
            print("The computer hit your ship!")
            return True
        else:
            print("The computer missed!")
            return False
        #print(self.computer.print_board())
        #print(self.player.print_without_ships())
game = Game()

#game start
while (game.game):
    game.intro()
    game.insert_all_ship()
    turn = 1
    t = random.choice([1, 2])
    while turn == 1:
        
        if t == 1:
            print("Your turn: ")
            if game.player_turn():
                t = 1
            else:
                t = 2
        elif t == 2:
            print("Computer's turn: ")
            time.sleep(3)
            if game.computer_turn():
                t = 2
            else:    
                t = 1
        if game.player.if_all_sunk():
            print("You lost!")
            turn = 0
        elif game.computer.if_all_sunk():
            print("You won!")
            turn = 0
        print("Your board: ")
        print(game.player.print_board())
        print("Computer board: ")
        print(game.computer.print_without_ships())
    


        
    do = input("Do you want to play again? (y/n)")
    if do == "n":

        game.game = False
    


