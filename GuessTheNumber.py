import random


def start(first_call):
    # Just to make sure it's a valid response
    if first_call == 0:
        play = str(input("Do you want to play a game? (y/n): \n"))
    else:
        play = first_call
    while play != "y" and play != "n":
        print("what?")
        play = str(input())
    if play == "y":
        random_num_game()
        replay = str(input("\nThanks for playing! Would you like to play again? (y/n): "))
        start(replay)
    elif play == "n":
        print("That's too bad")


def wincon(guess, num, turn):
    # checking if the number was too high, low, or correct
    if guess > num:
        if turn == 5:
            print("\nThat's too high")
        else:
            print("\nThat's too high, guess again:")
    elif guess < num:
        if turn == 5:
            print("\nThat's too low")
        else:
            print("\nThat's too low, guess again:")
    elif guess == num:
        return str("winner")


def random_num_game():
    # Setup and checking for win/lose condition
    turn = 0
    print("I'm guessing of a number between 1 and 20, can you guess it?\n\nguess a number: \n")
    num = (random.randint(1, 20))

    while turn != 7:
        turn += 1
        if turn == 6:
            break
        guess = int(input())
        win = wincon(guess, num, turn)
        if win == "winner":
            break

    if turn == 6:
        print("\nYou lose!\nthe number was ", num)
    else:
        return print("\nThat's the one!")


start(0)
