import random


def hint_output():print(f'''I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.''')


def get_guess(guess_num):
    """- Get the guess from the user
       - Validate if the guess is 3 unique digits
    Args:
        guess_num (int): The number of guess the current guess is

    Returns:
        guess (str): a string of three unique digits
    """
    print(f'Guess #{guess_num}')
    guess = input('> ')
    while not guess.isdigit() or len(guess) != 3 or len(set(guess)) != len(guess):
        print(f'Guess #{guess_num}')
        guess = input('> ')
    return guess


def message():print(f'''I have thought up a number.
 You have 10 guesses to get it.''')


def gen_rand_num():
    """Generate a random 3 integer list

    Returns:
        list: list of 3 unique integers
    """
    begels_rand = random.sample(range(0,10),3)

    return begels_rand


def loop_body(guess,begels_num):
    """The body of the for loop, this function will be called inside a loop

    Args:
        guess (str): a string of 3 unique digits
        begels_num (list): list of 3 unique integers

    Returns:
        bool : True if the guess is correct else false
    """
    
    correct = 0
    incorrect = 0
    for i in range(3):
        if guess[i] == str(begels_num[i]):
            print('Fermi',end=' ')
            correct += 1
        elif int(guess[i]) in begels_num:
            print('Pico',end=' ')
            incorrect += 1
    
    if correct == 0 and incorrect == 0:print('Begels',end=' ')
    print('')
    if correct == 3: return True
    return False


def loop_begels(begels_num):
    """main loop of the begels, running a maximum span of 10 guesses
        breaks if the user guesses correct

    Args:
        begels_num (list): list of 3 unique integers

    Returns:
        bool: True if the user guessed correctly, False if all 10 guesses were wrong
    """
    for i in range(0,10):
        guess = get_guess(i+1)
        if loop_body(guess,begels_num):return True
    return False


def verdict_message(verdict,begels_num):
    
    if verdict:print('You got it!')
    else: print(f'''You Failed
The correct answer was {''.join(map(str, begels_num))}''')


def play_again():
    """Prompt if user they want to play again

    Returns:
        bool: True if yes and False if no
    """
    while True:
        play = input('Do you want to play again? (yes or no): ')
        if play.lower() == 'yes':return True
        elif play.lower() == 'no':return False


def main_begels():
    play = True
    while play:
        hint_output()
        begels_num = gen_rand_num()
        print(begels_num)
        message()
        verdict = loop_begels(begels_num)
        verdict_message(verdict,begels_num)
        play = play_again()
    print('Thanks for playing!')

if __name__ == '__main__': main_begels()
