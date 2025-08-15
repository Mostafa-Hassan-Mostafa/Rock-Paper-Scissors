import random
options = ("rock", "paper", "scissors")
running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): \n")
    print(f"Player: {player}")
    print(f"Computer: {computer}")
#Output options
    if player == computer:
       print("It's a TIE!")
    elif player == "rock" and computer == "scissors":
       print("You WIN!")
    elif player == "paper" and computer == "rock":
       print("You WIN!")
    elif player == "scissors" and computer == "paper":
       print("You WIN!")
    else:
       print("You LOSE!")
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "no":
        running = False
print("Thanks for playing")