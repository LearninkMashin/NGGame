import random, time 
introtext = """Welcome to Kağan's number guessing game! 

I will think of a number between 1 and 100. 

I'll give you a few tries to guess the correct number! 
To start, choose your difficulty: 
1. Easy (10 tries) 
2. Medium (5 tries) 
3. Hard (3 tries)

You will receive 4 HINTS that do not waste a guess.
"""


levelmap = {"1": 10, "2": 5, "3": 3}

#Choose difficulty because it also determines the amount of tries the player gets
def NMGdifficulty():
     levelmap = {"1": 10, "2": 5, "3": 3}
     while True:  # keep looping until we "break"
        level_choice = input("\nSo, what level do you want to play at?\n").strip()

        if level_choice in levelmap:
            tries = levelmap[level_choice]
            if level_choice == "1" :
                print("\nYou have chosen Easy difficulty, good luck!")
            elif level_choice == "2":
                print("\nThe middleground huh? Well, goodluck!")
            elif level_choice == "3":
                print("\nGood luck losing, all due respect!!")
            return tries
        else: 
            print("You did not pick a difficulty, please type only one number.")
        



def numberguessing(tries):
    number = random.randint(1, 100)
    print("\nNow that you've made up your mind on your difficulty I have thought of a number between 1 and 100, take a guess")
    hints_used = 0

    for attempt in range(1, tries + 1):
        while True:
            guess_str = input(f"Guess {attempt}/{tries} (type 'hint or h' for hint): ").strip()

            if guess_str.lower() in ("hint", "h"):

                hint_steps = [
                    lambda: print("Hint: The number is", "even." if number % 2 == 0 else "odd."),
                    lambda: print("Hint: The number is", "greater than 50." if number > 50 else "less than or equal to 50."),
                    lambda: (lambda low, high: print(f"Hint: It’s between {low} and {high}"))((number // 10) * 10, (number // 10) * 10 + 9),
                    lambda: (lambda low, high: print(f"Final hint: It’s somewhere between {low} and {high}"))(max(1, number - 5), min(100, number + 5))
                ]

            # Choose the right hint (if out of range, just repeat the last one)
                index = min(hints_used, len(hint_steps) - 1)
                hint_steps[index]()   
                hints_used += 1
                continue


            if guess_str.isdigit():
                guess = int(guess_str)
                break
            print("Please enter a whole number between 1 and 100, or type 'hint'.")

        if guess == number:
            print(f"\n🎉 Correct! The number was {number}. You did it in {attempt} guesses.")
            return True
        print("Too low!" if guess < number else "Too high!")

    print(f"\nToo bad! The number was {number}. Better luck next time.")
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
        start = time.time()                
        result = numberguessing(tries)
        elapsed = time.time() - start      

        print(f"You spent {elapsed:.2f} seconds this round.")


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