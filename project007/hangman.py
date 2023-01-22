import hangman_art
import hangman_words
import random

print(hangman_art.logo)
selected_word = random.choice(hangman_words.word_list)
# selected_word = random.choice(hangman_words.marvel_heroes)
# selected_word = random.choice(hangman_words.python_builtin_functions)
# print(selected_word)

displayed_letter_list = []
for letter in selected_word:
    if letter == ' ':
        displayed_letter_list.append(' ')
    else:
        displayed_letter_list.append('_')
        
# print(displayed_letter_list)
displayed_word = ''.join(displayed_letter_list)
# print(displayed_word)

lives = 6
for index in range(lives):
    while True:
        guessed_letter = input('Guess a letter: ').lower()
        if guessed_letter in displayed_word:
            print(f"You've already guessed {guessed_letter}")
        else:
            break
    if guessed_letter not in selected_word:
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
    else:
        for idx in range(len(selected_word)):
            if selected_word[idx] == guessed_letter:
                displayed_letter_list[idx] = guessed_letter
        displayed_word = ''.join(displayed_letter_list)
    print(displayed_word)
    if displayed_word == selected_word:
        print('You win.')
        break
    elif index == lives - 1:
        print('You lose.')
        break
    print(hangman_art.stages[index])

# print(selected_word)