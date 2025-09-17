import random
text = """Welcome to Kağan's number guessing game! 

I will think of a number between 1 and 100. 

I'll give you a few tries to guess the correct number! 
To start, choose your difficulty: 
1. Easy (10 tries) 
2. Medium (5 tries) 
3. Hard (3 tries)"""
print(text)


def NMGintro():
     while True:  # keep looping until we "break"
        print("So, what level do you want to play at?")
        level_choice = input()
        if level_choice == "1" :
            print("You have chosen Easy difficulty, good luck!")
        elif level_choice == "2":
            print("The middleground huh? Well, goodluck!")
        elif level_choice == "3":
            print("Good luck losing, all due respect!!")
        else: 
            print("You did not pick a difficulty, please type only one number.")
            continue
        
        break

def numberguessing():
    number = random.randrange(1, 101)
    guessestaken = 0 
    print("Now that you've made up your mind on your difficulty I have thought of a number between 1 and 100, take a guess")
    guess = input()
    
NMGintro()
numberguessing()