import random

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """

    guess =(current_low + current_high)//2

    return guess

def pick_number():

    print("Think of a number between " + str(low) + " and " + str(high) + " then Press the ENTER key to continue.")

    con = input()
        
    
def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """ 

    answer = input("Is the number " + str(guess) + " too high, too low, or correct ")
    
    if answer == 'too high' or answer == 'high':
        return 1
    
         
    if answer == 'too low' or answer == 'low':
        return -1


    if answer == 'correct':
        return 0




          
def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()

    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            # adjust current_low
            current_low = guess + 1
        elif check == 1:
            # adjust current_high
            current_high = guess - 1

    show_result()


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



