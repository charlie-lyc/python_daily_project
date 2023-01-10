import hangman_art
import hangman_words
import random

print(hangman_art.logo)
selected_random_word = random.choice(hangman_words.marvel_heroes)
# selected_random_word = random.choice(hangman_words.python_builtin_functions)
# selected_random_word = random.choice(hangman_words.word_list)

# displayed_letter_list = []
displayed_word = ''
for letter in selected_random_word:
    if letter == ' ':
        # displayed_letter_list.append('-')
        displayed_word += '-'
    else:
        # displayed_letter_list.append('_')
        displayed_word += '_'

# displayed_word = ''.join(displayed_letter_list)
print('Random word:', displayed_word)
##################################################################
# displayed_letter_list = displayed_word.split('') # NOT AVAILABLE
displayed_letter_list = list(displayed_word)
##################################################################

chances = 7
used_life = 0
for _ in range(chances):
    print(hangman_art.stages[used_life])
    guessed_letter = input('Guess a letter: ').lower()
    for idx in range(len(selected_random_word)):
        if selected_random_word[idx] == guessed_letter:
            displayed_letter_list[idx] = guessed_letter
    #############################################################
    # displayed_word = str(displayed_letter_list) # NOT AVAILABLE
    displayed_word = ''.join(displayed_letter_list)
    #############################################################
    print('Random word:', displayed_word)
    if displayed_word == selected_random_word:
        print('You win.')
    used_life = used_life + 1
    
print('You lose.')
print(f"Random word was '{selected_random_word}'.")
