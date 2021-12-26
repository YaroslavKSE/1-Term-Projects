import random
name_of_the_game = 'H A N G M A N'
statement = 'You have got 6 tries'
print(f'{name_of_the_game}\n{statement}')


def secret_word():
    secret_world = ['python', 'java', 'kottlin', 'javascript', 'funny', 'galaxy', 'gossip'
                    'icebox', 'jelly', 'puppy', 'staff', 'football', 'tiger', 'lizard']
    index = random.randint(0, secret_world.index(secret_world[-1]))
    word_to_guess = secret_world[index]
    return word_to_guess


def game(word_to_guess):
    hidden_word = "-" * len(word_to_guess)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    print(hidden_word)
    while not guessed and tries > 0:
        player_input = input("Iput a letter or a word:")
        if len(player_input) == 1 and player_input.isalpha():
            if player_input in guessed_letters:
                print("You've already guessed the letter", player_input)
            elif player_input not in word_to_guess:
                print(player_input, "is not in the word")
                tries -= 1
                guessed_letters.append(player_input)
            else:
                print("Well done", player_input, "is in the word")
                guessed_letters.append(player_input)
                word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(word_to_guess) if letter == player_input]
                for index in indices:
                    word_as_list[index] = player_input
                hidden_word = "".join(word_as_list)
                if "-" not in hidden_word:
                    guessed = True
        elif len(player_input) == len(word_to_guess) and player_input.isalpha():
            if player_input in guessed_words:
                tries -= 1
                print("You've already guessed the word", player_input)
            elif player_input != word_to_guess:
                print(player_input, "is not the word")
                tries -= 1
                guessed_words.append(player_input)
            else:
                guessed = True
                hidden_word = word_to_guess

        else:
            print("That letter doesn't appear in the word")
        print(hidden_word)
    if guessed:
        print("Good job. You've survived")
    else:
        print(f"You are out of tries. You'are hanged\nThe word was: {word_to_guess}")


def main():
    word_to_guess = secret_word()
    game(word_to_guess)
    while input("Do you wanna play one more game (Yes/No)") == "Yes":
        word_to_guess = secret_word()
        game(word_to_guess)


main()
