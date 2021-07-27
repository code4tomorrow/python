# Directions: Lets Play Hangman. In the code, create a certain
# word that the user has to guess the word in 15 guesses
# similar to the original game of hangman


def hangman():
    global score
    endword = "hangman"
    wordSet = set(endword)
    print(
        "Welcome to Hangman! You have 15 guesses to "
        + "figure out the correct word. Good Luck!"
    )

    guesses = 15
    correctguesses = []

    for i in range(15):
        guess = input(
            "Guess a letter!" + "You have " + str(guesses) + " guesses left:"
        )
        if guess == endword:
            print("Nice, the word is 'hangman'")
            break

        if guess in endword:
            correctguesses.append(guess)
        for i in range(len(endword)):

            if endword[i] in correctguesses:
                print(endword[i], end="")
            else:
                print("_ ", end="")
        print()
        if guess != wordSet:
            guesses -= 1

        if guesses == 0:
            print("You ran out of guesses. The correct word is hangman")
        if set(correctguesses) == wordSet:

            print("Nice, the word is 'hangman'")
            score += 1
            break
