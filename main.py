import random
guessNo = random.randint(1, 100)
guesses = 10
i = 0
print("\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to Guessing Game!!")
print("\t\t\t\t\t\t\t\t\t\t\t  You have %s guesses to guess the number" % guesses)
while i < 14:
    if guesses == 0:
        print("\nGame Over!!")
        break
    inp = int(input("\nGuess the secret number\n"))
    if inp == guessNo:
        guesses -= 1
        print("\nYour guess is correct\nYou took", 10-guesses, "guess to finish the game", "\nYou Won!!")
        break
    elif inp < guessNo:
        guesses = guesses - 1
        print("No.. Guess the greater number")
        print("Number of guesses left:", guesses)
        i = i + 1
        continue
    elif inp > guessNo:
        guesses = guesses - 1
        print("No.. Guess the lesser number")
        print("Number of guesses left:", guesses)
        i = i + 1
        continue
