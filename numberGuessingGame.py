import random
number = random.randint(0,10)
chances = 0

while chances < 5 : 
    guess = int(input("Enter your guess"))
    chances = chances + 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    print('CONGRATULATIONS!! You guessed the number correct.')
else: 
    print("You lost!! Please try again.")

    
    
        

    


