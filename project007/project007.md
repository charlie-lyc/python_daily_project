# [Hangman Game]('https://en.wikipedia.org/wiki/Hangman_(game)')

<hr />

## [Play Game]('https://hangmanwordgame.com')
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

## Step 1
Select a word randomly from the word list of ```hangman_words``` module.

## Step 2
Create blanks with under score(```_```) as the same length of the random word selected from the word list.

If the random word is ```'python'```, the word displayed on screen is:
```
Random Word: _ _ _ _ _ _
```

However, if the random word includes space string(```' '```), replace it with dash(```'-'```).

If the random word is ```'iron man'```, the word displayed on screen is:
```
Random Word: _ _ _ _ - _ _ _
```

## Step 3
Import the stage of the game from the ```hangman_art``` module.

Repeat this at the beginning of each stage.
```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
```

## Step 4
Input a letter the user guessed and make it lowercase.

```
Guess a letter: 
```

## Step 5
The user can have 7 chances and must check at each chance if the letter the user guessed is one of the letters in the random word selected from word list.

If the letter the user guessed is one of the letters in the random word selected word list, replace an under score with the letter.
```
Guess a letter: o
Random word: _ _ _ _ o _
```

Otherwise:
```
Guess a letter: e
Random word: _ _ _ _ _ _
```

## Step 6
Playing the game, if the word displayed on screen is the same as the random word selected from word list, print ```You win.```.
```
Random word: p y t h o n
You win.
```

## Step 7
After using all chances, print ```You lose.```.

Then print the random word selected from word list.
```
Random word: p _ t h o _
You lose.
Random word was 'python'.
```