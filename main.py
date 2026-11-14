import core
import ui

screen = ui.setup_screen()
ui.draw_track()
turtles = ui.create_turtles()

money = core.START_MONEY   # resets to 500 every time the program runs

while money > 0:
    print(f"\nYou have {money} pesos.")
    bet = core.ask_bet(money)
    choice = core.ask_turtle()

    ui.reset_turtles(turtles)
    winner = core.run_race(turtles)
    money = core.settle(money, bet, choice, winner)

    result = "WIN" if choice == winner else "LOSE"
    print(f"{core.color_name(winner).upper()} won! You {result}. Pesos: {money}")

    if money > 0 and input("Race again? (y/n): ").lower() != "y":
        break

print(f"\nGame over. You finished with {money} pesos.")
screen.bye()