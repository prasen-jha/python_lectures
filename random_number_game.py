from random import randint

print('''  It's a guessing game
            You will get 8 tries and number is between 1 to 100
            you have to guess the number which has been set by the system''')

winning_number = randint(1,101)
TRIES = 8

for _ in range(TRIES):
    guess = int(input('Enter Your Guess: '))

    if guess == winning_number:
        print('You Won ! what a Player!')
        break
    elif guess < winning_number:
        print('Guess is Low')
    elif guess > winning_number:
        print('Guess is High')
else:
    print(f'You lost ! what a loser! :( tho the answer was {winning_number}')