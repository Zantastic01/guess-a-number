import random
import math



def show_start_screen():
    print(" ██████╗ ██╗   ██╗███████╗███████╗███████╗     █████╗     ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      █████╗    ██╗  " )
    print("██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ██╔══██╗    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔══██╗   ██║   ")
    print("██║  ███╗██║   ██║█████╗  ███████╗███████╗    ███████║    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ███████║   ██║   ")
    print("██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║    ██╔══██║    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██╔══██║   ██║   ")
    print("╚██████╔╝╚██████╔╝███████╗███████║███████║    ██║  ██║    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ██║  ██║██╗██║██╗")
    print(" ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚═╝╚═╝")
                                                                                                                                     
def show_credits():
    print("                     _           _   _              ")                                          
    print("   ___ _ __ ___  __ _| |_ ___  __| | | |__  _   _ ")
    print("  / __| '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | |")
    print(" | (__| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |")
    print("  \___|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, |")
    print("                                            |___/ ")
 
    print(" _______  _______  __    _    __   __  _______  __    _ ")
    print("|       ||   _   ||  |  | |  |  |_|  ||   _   ||  |  | |")
    print("|____   ||  |_|  ||   |_| |  |       ||  |_|  ||   |_| |")
    print(" ____|  ||       ||       |  |       ||       ||       |")
    print("| ______||       ||  _    |  |       ||       ||  _    |")
    print("| |_____ |   _   || | |   |  | ||_|| ||   _   || | |   |")
    print("|_______||__| |__||_|  |__|  |_|   |_||__| |__||_|  |__|")
                                                                                     
    
def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """

    guess =(current_low + current_high) // 2
    return guess

    
def pick_number(low, high, limit):
    print("Please think of a number between " + str(low) + " and " + str(high) +
    " and I will get a total of " + str(limit) + " tries. Press the ENTER key to continue.")
    input()
    
           
def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """ 
    while True:
        print("Is the number " + str(guess) + " too high, too low, or correct? ")
        answer = input()
        answer = answer.lower()
    
        if answer == 'too high' or answer == 'h' :
            return 1
        elif answer == 'too low' or answer == 'l':
            return -1
        elif answer == 'correct' or answer == 'c':
            return 0
        else: 
            print("I don't understand. Please enter 'too high', 'too low', or 'correct'.")



          
def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    print("I win!")
          

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    print (" What's the highest value I can guess?")
    current_high = input()
    current_high = int(current_high)
    
    print(" Now whats the lowest value I can guess?")
    current_low = input()
    current_low = int(current_low)
    
    check = -1
    limit = math.ceil(math.log(current_high - current_low +1,2))
    
    pick_number(current_low, current_high, limit)
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            # adjust current_low
            current_low = guess
        elif check == 1:
            # adjust current_high
            current_high = guess

    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



