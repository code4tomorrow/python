# Directions: Lets Play Hangman. In the code, create a function that
# takes as a paramater the word that the user has to guess.
# The user should have 15 'lives'.
# Similar to the original game of hangman, if the user guesses an incorrect
# letter, then their lives goes down. If they guess a correct letter, they
# don't lose a life.


score = 0


def hangman(endword: str):
    global score
    wordSet = set(endword)
    print(
        "Welcome to Hangman! You have 15 guesses to "
        + "figure out the correct word. Good Luck!"
    )

    guesses = 15
    correctguesses = []

    # mainloop
    for i in range(15):
        # take user input
        guess = input("Guess a letter! You have " + str(guesses) + " guesses left: ")

        # win condition
        if guess == endword:
            print(f"Nice, the word is '{endword}'")
            score += 1
            break

        if guess in endword:
            correctguesses.append(guess)

        # 'draw screen' phase
        for i in range(len(endword)):
            if endword[i] in correctguesses:
                print(endword[i], end="")
            else:
                print("_ ", end="")
        print()

        if guess not in wordSet:
            guesses -= 1

        # update game state
        # game over condition
        if guesses == 0:
            print(f"You ran out of guesses. The correct word is '{endword}'")

        # win condition
        if set(correctguesses) == wordSet:
            print(f"Nice, the word is '{endword}'")
            score += 1
            break


hangman("hangman")
