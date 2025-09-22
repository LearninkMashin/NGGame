import random
introtext = """Welcome to Kağan's number guessing game! 

I will think of a number between 1 and 100. 

I'll give you a few tries to guess the correct number! 
To start, choose your difficulty: 
1. Easy (10 tries) 
2. Medium (5 tries) 
3. Hard (3 tries)"""


levelmap = {"1": 10, "2": 5, "3": 3}

#Choose difficulty because it also determines the amount of tries the player gets
def NMGdifficulty():
     levelmap = {"1": 10, "2": 5, "3": 3}
     while True:  # keep looping until we "break"
        level_choice = input("\nSo, what level do you want to play at?\n").strip()

        if level_choice in levelmap:
            tries = levelmap[level_choice]
            if level_choice == "1" :
                print("You have chosen Easy difficulty, good luck!")
            elif level_choice == "2":
                print("The middleground huh? Well, goodluck!")
            elif level_choice == "3":
                print("Good luck losing, all due respect!!")
            return tries
        else: 
            print("You did not pick a difficulty, please type only one number.")
            


        
def numberguessing(tries):
    number = random.randint(1, 100)
    print("\nNow that you've made up your mind on your difficulty I have thought of a number between 1 and 100, take a guess")

    for attempt in range(1, tries + 1):
            while True:
                guess_str = input(f"Guess {attempt}/{tries}: ").strip()
                if guess_str.isdigit():
                    guess = int(guess_str)
                    break
                print("Please enter a whole number between 1 and 100.")

            if guess == number:
                print(f"🎉 Correct! The number was {number}. You did it in {attempt} guesses.")
                return True
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")

    print(f"Too bad! The number was {number}. Better luck next time.")
    return False


def ask_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer y or n.")

def main():
    rounds = 0
    wins = 0

    print(introtext)

    tries = NMGdifficulty()
    while True:
        result = numberguessing(tries)
        rounds += 1
        if result:
            wins += 1
        if not ask_yes_no("Play again? (y/n): "):
            break
        if not ask_yes_no("Keep the same difficulty? (y/n): "):
            tries = NMGdifficulty()
    
    
    print(f"\nThanks for playing! You won {wins} out of {rounds} rounds.")

  
    

if __name__ == "__main__": 
    main()