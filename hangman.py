import random
wrds = ["python", "programming", "computer", "hangman", "loops", "functions", "conditionals", "boolean"]



def choose_word(wrds):
    return random.choice(wrds)
    
    
def display_word(word, guesses):
    display = "" #
    for i in word:
        if i in guesses:
            display += i
        else:
            display += "_"
            
    return display
    
def get_guess(guesses):  #Can't input a letter twice {run into problems}
    guess = input("Input guess: ")
    if guess.isalpha() and guess not in guesses and len(guess) == 1:
        return guess
    else:
        print("You already entered that letter, try again.")

    

def hangman():
    print("Welcome to Hangman!")
    #impliment get_guess in hangman
    guesses = []
    i = 6
    word = choose_word(wrds)
    while i > 0:
        guess = get_guess(guesses) #sets a variable to the output of get_guess
        guesses.append(guess) #adds element to the list
        display = display_word(word,guesses)
        print(display)
        if guess not in word:
            i -= 1
        print(f"You have {i} incorrect guesses left.")
        print(f"Guessed letters: {guesses}")
        
        if "_" not in display:
            print("I won")
            break 
    print("You lost")
    
        

         
    
hangman()