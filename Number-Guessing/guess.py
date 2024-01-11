import random
def play_game():
    max_num = 20

random_number = random.randint(1, max_num)
guess = 0

while True:
    guess = int(input(f"Guess the number between 1 & {max_num} or type 'quit' to exit: "))
    if guess == random_number:
        print(f"That Right! Random number is {random_number}")
    elif guess < random_number:
        print("Wrong! Too Low...")
    elif guess > random_number:
        print("Wrong! Too High...")   
    else:
        break
play_game()