import random
def guess_number_game():
    name=input("Heloo,what is your name?")
    target_num=random.randint(1,20)
    
    guesses=0
    while True:
        print("Take a shot : ")
        guess=int(input())
        guesses+=1
        
        
        if guess < target_num:
            print("Your guess is too low.")
        elif guess > target_num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break     
    
    