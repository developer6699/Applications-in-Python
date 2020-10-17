from random_word import RandomWords
r = RandomWords()

# Return a single random word
word = r.get_random_word().lower()
wordLength = len(word)


# Guessed
guessed = []


def rules(name):
    print(f'Hi {name}, Welcome to the Guess game.\n')

    print("Rule 1: There might be more than single words, use - instead of space.")
    print("Rule 2: Get to guess single letter in each try.")
    print(f'Rule 3: Guess the word in {wordLength+3} tries otherwise you loose the game.\n')
    print(f'This is a {wordLength} letter word.')


def guess():
    for a in word:
        guessed.append("_")
    print(*guessed)

    guess_number = try_number = 0
    d = wordLength + 3

    while try_number < wordLength+3:
        user_input = input('guess the letter: ')
        for i in range(0, wordLength):
            if user_input in word[i]:
                if user_input in guessed:
                    try_number += 1
                    print("Oops! " + user_input + " already typed this letter earlier.")
                    d -= 1
                    print(f'{d} tries left.\n')
                guessed[i] = user_input
                guess_number += 1
                print(f'{d} tries left.\n')

            elif user_input not in word:
                try_number += 1
                print("Oops! " + user_input + " is not in the word")
                d -= 1
                print(f'{d} tries left.\n')
                break

        if guess_number == wordLength and word in guessed:
            print("Congrats!, you guessed")
            break
        print(*guessed)

    print(word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rules('Player')
    guess()
