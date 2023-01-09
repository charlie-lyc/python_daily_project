import hangman_art
import hangman_words
import random

print(hangman_art.logo)
selected_random_word = random.choice(hangman_words.marvel_heroes)
# selected_random_word = random.choice(hangman_words.python_builtin_functions)
# selected_random_word = random.choice(hangman_words.word_list)

displayed_letters_list = []
for letter in selected_random_word:
    if letter == ' ':
        displayed_letters_list.append('-')
    else:
        displayed_letters_list.append('_')
print('Random word:', ' '.join(displayed_letters_list))

chances = 7
used_life = 0
for _ in range(chances):
    print(hangman_art.stages[used_life])
    guessed_letter = input('Guess a letter: ').lower()
    for idx in range(len(selected_random_word)):
        if selected_random_word[idx] == guessed_letter:
            displayed_letters_list[idx] = guessed_letter
    print('Random word:', ' '.join(displayed_letters_list))
    if ''.join(displayed_letters_list) == selected_random_word:
        print('You win.')
    used_life = used_life + 1
    

print('You lose.')
print(f"Random word was '{selected_random_word}'.")
