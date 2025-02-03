print("Welcome to Quiz Game")
start = input("Do you wanna Play Quiz Game(yes/no):").lower()

if start != "yes":
    quit()

print("OKK!!!!, Let's Play the game")

question = {
    "1947":"When was pakistan got independet?",
    "2005":"When was Mussadiq Born?",
    "round":"Is earth round or flat?"
}
score = 0
for key, value in question.items():
    print(value)
    ans = input("Answer: ").lower()
    if ans == key:
        print("Correct")
        score +=1
    else:
        print("Incorrect")
        
print(f"Your Score is {score}")