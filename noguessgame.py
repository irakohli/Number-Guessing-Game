import random 
random=random.randint(0,100)
print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 0 and 100.")
print("Try to guess the number, I will tell you if your guess is too high or too low!")
print("You can keep guessing until you want to stop.")
while True:
    guess = int(input("Enter your guess: "))
    if guess < random:
        print("Too low! Try again.")
    elif guess > random:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number!")
        break
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        print("Thanks for playing! Goodbye!")
        break
