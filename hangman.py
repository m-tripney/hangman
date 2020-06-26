from random import choice
from string import ascii_lowercase


def check_input(guess_string, guessed_letters):
    if len(guess_string) != 1:
        print("You should input a single letter.")
        return False
    elif guess_string not in ascii_lowercase:
        print("It is not an ASCII lowercase letter.")
        return False
    elif guess_string in guessed_letters:
        print("You already typed this letter.")
        return False
    return True


word = choice(["python", "java", "kotlin", "javascript"])
hidden = list(len(word) * "-")
counter = 0
guesses = []

print(" ".join("HANGMAN"))
while True:
    play_exit = input("Type 'play' to play the game, 'exit' to quit: ")
    if play_exit not in ["play", "exit"]:
        continue
    elif play_exit == "exit":
        break
    else:
        while counter < 8 and "-" in hidden:
            guess = input(f"\n{''.join(hidden)}\nInput a letter: ")
            if check_input(guess, guesses):
                guesses.append(guess)
                if guess in word:
                    indices = [
                        index for index in range(len(word)) if word[index] == guess
                    ]
                    for index in indices:
                        hidden[index] = guess
                else:
                    print("No such letter in the word.")
                    counter += 1
            else:
                continue

        if "-" not in hidden:
            print(f"\n{word}\nYou guessed the word!\nYou survived!")
        else:
            print("You are hanged!")
