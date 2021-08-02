import random

print('Welcome to the Number Guessing games!')
print("I'm thinking of a number between 1 and 100")

def play():
  selection = True
  while selection:
    Difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attemps = 0
    if Difficulty.lower() == 'easy':
      attemps = 10
      selection = False
    elif Difficulty.lower() == 'hard':
      attemps = 5
      selection = False

  number = random.randint(1,100)
  game = True
  while game:
    print(f'You have {attemps} remaining to guess the number')
    guess = int(input('Make a guess: '))

    if guess == number:
      print(f'You won with {attemps} remaining')
      game = False
    elif guess < number:
      print('Too low')
      attemps -= 1
    else:
      print('Too high')
      attemps -=1
    
    if attemps == 0:
      print(f'You lose, the number was :{number}')
      game = False


play()
play_again = input('Do you wanna play again? Type Y or N ')
if play_again.lower() == 'y':
  play()
