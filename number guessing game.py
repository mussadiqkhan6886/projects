from random import randint

print("Welcome To Number Guessing Game")

number = randint(0, 20)

guesses = 0

while True:
    guesses += 1
    guess = int(input("Enter Number: "))
    if guess != number:
        print("Incorrect")
        if guess > number:
            print("Take a lower nunmber next time")
        else:
            print("Take a higher number next time")
    else:
        print("CORRECT!!!!")
        break
        
print(f"You Gueesed in {guesses} guesses")