import random
x = random.randint(1,100)

print('A number from 1 to 100 has been picked.\nYour guess within 10 of that num will be WARM and COLD otherwise\nSubsequent guesses will be warmer or colder based on prev guess')

guess_list = []

while True:
    while True:
        try:
            guess = int(input('Please guess a number between 1 and 100.\n'))
        except:
            print('Please enter a valid integer')
            continue
        if guess not in range(101):
            print('Number not in range 1-100. Please try again')
            continue
        else:
            break
    guess_list.append(guess)
    diff = abs(guess_list[-1]-x)
    if guess_list[-1] == x:
        print(f'Correct guess, the number was {x}.')
        print(f'You took {len(guess_list)} attempts to guess correctly')
        print(guess_list)
        guess_list.clear()
        break
    elif len(guess_list) == 1 and diff in range(11):
        print('Warm')
    elif len(guess_list) == 1 and diff not in range(11):
        print('Cold')
    else:
        old_diff = abs(guess_list[-2]-x)
        if diff<=old_diff:
            print('Warmer')
        else:
            print('Colder')