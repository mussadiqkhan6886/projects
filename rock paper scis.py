import random

print("WELCOME TO ROCK PAPER SCCISSOR GAME")

def main():
    li = ["rock", "paper", "scissor"]
    computer = random.choice(li)
    
    player = input("Enter rock, paper, scissor: ").lower()
    if player not in li:
        print("Choose rock paper or scissor")
        quit()
        
    if player == computer:
        print("Its Tie")
    else:
        if player == "rock" and computer == "paper":
            print("You Lose")
        elif player == "paper" and computer == "scissor":
            print("You Lose")
        elif player == "scissor" and computer == "rock":
            print("You Lose")
        elif player == "rock" and computer == "scissor":
            print("You Win")
        elif player == "paper" and computer == "rock":
            print("You Win")
        elif player == "scissor" and computer == "paper":
            print("You Win")
        else:
            print("You Lose")
        
    print(f"You Choose {player} computer Choose {computer}")
    

if __name__ == "__main__":
    main()

