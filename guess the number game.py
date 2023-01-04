import random

num = random.randint(1, 10)
guess=None
while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    elif guess>=num:
        print('Number too high')
    elif guess<=num:
        print('Number too low')    
    else:
        print("nope, sorry. try again!")
        
