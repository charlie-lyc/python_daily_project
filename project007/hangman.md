# [Hangman Game](https://en.wikipedia.org/wiki/Hangman_(game))

<hr />

## [Play Game](https://hangmanwordgame.com)
- https://hangmanwordgame.com


<br>

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

<br>

## Preparation 1
Select a word randomly from the word list of ```hangman_words``` module.

<br>

## Preparation 2
Create blanks with under score(```'_'```) as the same length of the random word selected from the word list.

If the random word is ```'python'```, the word displayed on screen is:
```
_ _ _ _ _ _
```

<br>

## Step 1

Input a letter the user guessed and make it lowercase.

```
Guess a letter: p
```

If the letter is in the random word, replace under score with it in the same position on displayed word.
```
p _ _ _ _ _
```

Otherwise, print a message like below.
```
Guess a letter: a
```
```
_ _ _ _ _ _
You guessed a, that's not in the word. You lose a life.
```

<br>

## Step 2
At the end of an each stage, import the stage of the game from the ```hangman_art``` module.
```
Guess a letter: p
p _ _ _ _ _

  +---+
  |   |
      |
      |
      |
      |
=========
```
```
Guess a letter: a
You guessed a, that's not in the word. You lose a life.
p _ _ _ _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========
```

<br>

## Step 3
The user can have 6 chances and must check at each chance if the letter the user guessed is one of the letters in the random word selected from word list.

Playing the game, if the word displayed on screen is the same as the random word selected from word list, print ```You win.```.
```
Guess a letter: n
p y t h o n
You win.

  +---+
  |   |
  O   |
  |   |
      |
      |
=========
```

<br>

## Step 4
After using all chances, print ```You lose.```.

```
Guess a letter: u
You guessed u, that's not in the word. You lose a life.
You lose.
p _ _ _ _ _

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```
