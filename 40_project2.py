import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("your guessed it right!")
    else:
        if(userGuess>randNumber):
            print("you guessed it wrong! Enter a smaller number")
        else:
            print("you guessed it wrong! Enter a Larger number")
    

print(f"your guessed the number in {guesses} guesses")  
with open("highscore1.txt", "r") as f:
    highscore1 = int(f.read())

if(guesses<highscore1): 
    print("You broke the high score")
    with open("highscore1.txt", "w") as f:
      f.write(str(guesses)) 