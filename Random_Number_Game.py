import random
score_list = []

def start_game():
    random_number = random.randrange(1,10)
    name = input("<==== Hello there !! ====>\nWelcome to the number guessing game! \nWhat is your name?  ")
    try :
        score_list.sort()
        print(f'The current high score is {score_list[0]} attempt(s)..')
    except :
        print(f'Good luck, {name}!')
    attempt_count = 1
    guessed_number = input('Guess a number between 1 and 10:  ')

    try :
        guessed_number = int(guessed_number)
    except ValueError as err :
        print(f'Incorrect input. \n{err}')
        guessed_number = input('Try again.. Guess an integer between 1 and 10:  ')
        attempt_count += 1
    guessed_number = int(guessed_number)

    if guessed_number > 10 and guessed_number != random_number :
        print('Number out of range, please try again')
    elif guessed_number > random_number and guessed_number < 11 and guessed_number != random_number :
        print('Too high!')
    elif guessed_number < random_number and guessed_number != random_number :
        print('Too low!')

    while guessed_number != random_number :
        try :
                second_guess = int(input(f'Not quite, {name}..  Try again :'))
                if second_guess > 10 :
                    print('Number out of range')
                    attempt_count += 1
                    continue
                elif second_guess > random_number and second_guess < 11 :
                    print('Too high!')
                    attempt_count += 1
                    continue
                elif second_guess < random_number :
                    print('Too low!')
                    attempt_count += 1
                    continue
                elif second_guess > 10 :
                    print('Number out of range..')
                elif second_guess == random_number :
                    attempt_count += 1
                    print(f'Great job! It took you {attempt_count} tries to get it right!')
                    score_list.append(attempt_count)
                    break

        except ValueError as err :
            print(f'That is not a correct input.. We are looking for an integer.  \n{err}')
            attempt_count += 1

    if guessed_number == random_number :
        print(f'Wow, {name}, you did it first try! Congratulations!')
        score_list.append(attempt_count)

    play_again = input('Would you like to play again? (y/n)  ')
    if play_again == 'Y'.lower() :
        start_game()

start_game()

print('<=== Thanks for playing! ===>')
