import random

def guess_the_number():
    name = "KBTU"
    print(f"Hello! What is your name?\n{name}")
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    guesses_taken = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())  
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()