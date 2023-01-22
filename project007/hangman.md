# [Hangman Game](https://en.wikipedia.org/wiki/Hangman_(game))

<hr />

## [Play Game](https://hangmanwordgame.com)
- https://hangmanwordgame.com


## Start of The Game
Import the logo of the game from the ```hangman_art``` module.
```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
```

## Preparation 1
Select a word randomly from the word list of ```hangman_words``` module.

## Preparation 2
Create blanks with under score(```'_'```) as the same length of the random word selected from the word list.

If the random word is ```'python'```, the word displayed on screen is:
```
______
```

If the random word is ```'iron man'```, the word displayed on screen is:
```
____ ___
```

## Step 1

Input a letter the user guessed and make it lowercase.

```
Guess a letter: p
```

If the letter is in the random word, replace under score with it in the same position on displayed word.
```
p_____
```

## Step 2

Otherwise, print a message like below.
```
Guess a letter: a
```
```
You guessed a, that's not in the word. You lose a life.
______
```

## Step 3
The user can have 6 chances and must check at each chance if the letter the user guessed is one of the letters in the random word selected from word list.

Playing the game, if the word displayed on screen is the same as the random word selected from word list, print ```You win.```.
```
python
You win.
```

## Step 4
Import the stage of the game from the ```hangman_art``` module.

Repeat this at the end of each stage.
```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

## Step 5
After using all chances, print ```You lose.```.

```
p_tho_
You lose.
```