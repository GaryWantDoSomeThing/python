sym = [i for i in "yn"]
while True:
    while True:
        play = input("Would you like to play the Guessing Game: y/n ")
        if play is not None and play in sym:
            break
    if play == "y":
        attempts = 0
    elif play == "n":
        break
    # have fun, continue your game
    while True:
        numbToGuess = int(input("Player1 enter a number between 1 to 100:"))
        if play is not None and (numbToGuess >= 0 or play <= 100):
            break

    # guess loops
    while attempts < 7:

        # ensure the guess is a value
        while True:
            guess = int(input("Player2 enter a number to guess:"))
            if guess is not None:
                break
        attempts += 1
        if guess > 100:
            print(str(guess) + " is out of range, try guessing below 100: ")
        elif guess > numbToGuess:
            print(str(guess) + " is too high, guess again: ")
        elif guess == numbToGuess:
            print("Congratulation! You get it! ")
            attempts = 0
            break
        elif guess >= 0:
            print(str(guess) + " is too low, guess again: ")
        else:
            print(str(guess) + " is out of range, try guessing above 0: ")

    print("You failed, because you have out of choices!")
