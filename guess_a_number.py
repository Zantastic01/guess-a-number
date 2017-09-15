import random

#config
low = 1
high = 100
limit = 10

# start game
rand = random.randint(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high))

guess = -1
tries = 0

#helper functions
def get_guess():
        while True:
            g = input("Take a Guess: ")

            if g.isnumeric():
                g = int(g)
                return g
            else:
                print("You must enter a number")
                
# play the game
while guess != rand and tries < limit:
    guess = get_guess()
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    else:
        print("You got it!")

        tries += 1

# tell player outcome
if guess == rand:
    print("You win.")
else:
    print("You suck, i was thinking of "  + str(rand) + ".")
    
