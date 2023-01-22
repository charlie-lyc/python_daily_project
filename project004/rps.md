# Rock Paper Scissors

<hr />

## Instructions
Make a rock, paper, scissors game.

Inside the file, you'll use the ASCII art for the hand signals already saved to a corresponding variable: ```rock```, ```paper```, and ```scissors```. 
```python
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
```

This will make it easy to print them out to the console.

Start the game by asking the player:

```
What do you choose? 
Type 0 for Rock, 1 for Paper or 2 for Scissors.
```

From there you will need to figure out:

- How you will store the user's input.
- How you will generate a random choice for the computer.
- How you will compare the user's and the computer's choice to determine the winner (or a draw).
- And also how you will give feedback to the player.

<br />

## Example Input
```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
0
```

<br />

## Example Output
```
Computer chose:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
You win!
```

```
Computer's chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
You lose.
```

```
Computer's chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
It's a draw.
```

<br />

## Handling index out of range
```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
-1
```
```
Computer's chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
You typed an invalid number, you lose!
```

```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
3
```
```
Computer's chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
You typed an invalid number, you lose!
```

<br />

## Hint
You might have to do some Googling.

*[How to select a random integer in Python?](https://docs.python.org/3/library/random.html#random.randint)*

*[How to write conditional statements in Python?](https://www.w3schools.com/python/python_conditions.asp)*