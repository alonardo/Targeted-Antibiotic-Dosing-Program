import random

def rand():
    status = False
    correct = random.randint(0,10)
    correct = str(correct)
    print(f'Correct: {correct}')
    while status == False:
        guess = input('What number would you like to guess?\n')
        if guess == correct:
            print('Good job')
            status = True
            return status
        else:
            print('guess again')

rand()
