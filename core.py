import random
from ui import FINISH_X, COLORS

START_MONEY = 500

def ask_bet(money):
    while True:
        try:
            bet = int(input(f"Enter your bet (1 - {money}): "))
            if 1 <= bet <= money:
                return bet
        except ValueError:
            pass
        print("Invalid bet. Try again.")

def ask_turtle():
    print("1 - red, 2 - green, 3 - blue, 4 - yellow")
    while True:
        choice = input("Choose a turtle (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            return int(choice) - 1
        else:
            print("Invalid choice. Try again.")

def run_race(turtles):
    # each turtle moves a random distance every step;
    # the first one to cross the finish line wins
    while True:
        for i in range(4):
            turtles[i].forward(random.randint(1, 10))
            if turtles[i].xcor() >= FINISH_X:
                return i

def settle(money, bet, choice, winner):
    if choice == winner:
        return money + bet      # bet doubled: win = +bet
    else:
        return money - bet          # lose the bet

def color_name(index):
    return COLORS[index]